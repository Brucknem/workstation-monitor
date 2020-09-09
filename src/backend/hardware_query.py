import logging
import os
import re
import shlex
import subprocess
from datetime import datetime
from pathlib import Path

import pandas as pd
from systemd.journal import JournaldLogHandler

timestamp_format = f'%Y/%m/%d %H:%M:%S.%f'


class HardwareQuery:
    """Base class for hardware queries.
    """

    def __init__(self, logger: logging.Logger = None):
        """Constructor
        """
        self.timestamp = self.get_timestamp()
        self.subclass_name = self.__class__.__name__
        self.index_series = pd.Series(self.get_index())

        if logger:
            self.logger = logger
            return

        self.logger = logging.getLogger('workstation-monitor')
        journald_handler = JournaldLogHandler()
        journald_handler.setFormatter(
            logging.Formatter('[%(levelname)s] %(message)s'))
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(journald_handler)

    def get_timestamp(self):
        """Get the current timestamp.
        """
        return datetime.now()

    def get_bash_command(self) -> str:
        """The bash command used to query the hardware.
        """
        raise NotImplementedError('Implement the bash command')

    def get_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        complete_index = ['timestamp']
        complete_index.extend(self.get_custom_index())
        return complete_index

    def get_custom_index(self) -> list:
        """Gets the hardware specific indices that are added to the index.
        """
        return []

    def parse_query_result(self, result: str) -> pd.DataFrame:
        """Parse the query result.
        """
        raise NotImplementedError('Implement the parsing')

    def get_subclass_name(self) -> str:
        """Returns the name of the calling subclass.
        """
        return self.__class__.__name__

    def log(self, message: str, start: datetime, end: datetime):
        """Logs the message and appends the delta od the given timestamps.
        """
        delta = end - start
        seconds = delta.seconds
        microseconds = delta.microseconds
        self.logger.info(f'{message} [{seconds}.{microseconds}s]')

    def convert_to_numeric(self, dfs):
        """
        Converts the columns of the given dataframes to have as many numeric
        values as possible.

        :param dfs:
        :return:
        """
        converted = {}
        for name, df in dfs.items():
            for column in df.columns:
                if column == 'timestamp':
                    continue
                df[column] = df[column].apply(
                    lambda x: str(x).replace(',', '.') if bool(
                        re.search(r'[-+]?\d*\,\d+|\d+', x)) else x)
                df[column] = pd.to_numeric(df[column], errors='ignore',
                                           downcast='float')
            converted[name] = df
        return converted

    def query(self) -> dict:
        """Queries the hardware and creates a dataframe from it.
        """
        self.timestamp = self.get_timestamp()
        try:
            self.logger.info(f'Preforming a {self.subclass_name}')
            process = subprocess.Popen(shlex.split(self.get_bash_command()),
                                       stdout=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                raise FileNotFoundError(error)
            dfs = self.convert_to_numeric(
                self.parse_query_result(output.decode()))
            message = 'Successfully performed'
        except FileNotFoundError:
            message = 'Error performing'
        except subprocess.CalledProcessError:
            message = 'Error performing'

        self.log(f'{message} a {self.subclass_name}', self.timestamp,
                 self.get_timestamp())

        return dfs

    def query_and_update(self, output_path, file_type='json') -> list:
        """Queries the hardware, loads previous logs and appends the new values.
        """
        dataframes = self.query()
        start = self.get_timestamp()
        filenames = []
        for name, df in dataframes.items():
            Path(str(output_path)).mkdir(parents=True, exist_ok=True)
            full_path = os.path.join(str(output_path), name + '.' + file_type)
            filenames.append(full_path)

            if file_type == 'h5':
                self.update_h5(df, full_path)
            else:
                self.update_json(df, full_path)

        message = ", ".join(filenames)
        self.log(f'Written to {message}', start, self.get_timestamp())

        return filenames

    def update_h5(self, df: pd.DataFrame, full_path: str) -> None:
        if os.path.exists(full_path):
            with pd.HDFStore(full_path) as store:
                store.append('df', df)
            return

        df.to_hdf(full_path, key='df', mode='w', format='table')
        self.index_series.to_hdf(full_path, key='id')
        columns = list(df.columns)
        for index in self.get_index():
            columns.remove(index)
        columns = pd.Series(columns)
        columns.to_hdf(full_path, key='val')

    def update_json(self, df: pd.DataFrame, full_path) -> None:
        final_data = df
        if os.path.exists(full_path):
            previous_data = pd.read_json(full_path)
            final_data = pd.concat([previous_data, final_data])
            final_data.index = pd.RangeIndex(len(final_data.index))

        final_data.to_json(full_path)
