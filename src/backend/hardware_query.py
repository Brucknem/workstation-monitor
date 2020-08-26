import os
import shlex
import subprocess
import numpy as np
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime
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
        journald_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(message)s'
        ))
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
        return 

    def query(self) -> dict:
        """Queries the hardware and creates a dataframe from it.
        """
        self.timestamp = self.get_timestamp()
        try:
            self.logger.info(f'Preforming a {self.subclass_name}')
            process = subprocess.Popen(
                shlex.split(self.get_bash_command()),
                stdout=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                raise FileNotFoundError(error)
            dfs = self.parse_query_result(output.decode())
            self.logger.info(f'Successfully performed a {self.subclass_name}')
        except FileNotFoundError as e:
            self.logger.info(f'Error performing a {self.subclass_name}\n{e}')
        except subprocess.CalledProcessError as e:
            self.logger.info(f'Error performing a {self.subclass_name}\n{e}')

        # for key, frame in dfs.items():
        #     dfs[key] = frame.set_index(self.get_index())

        return dfs

    def query_and_update(self, output_path) -> list:
        """Queries the hardware, loads previous logs and appends the new values.
        """
        dataframes = self.query()
        filenames = []
        for name, df in dataframes.items():
            Path(str(output_path)).mkdir(parents=True, exist_ok=True) 
            full_path = os.path.join(str(output_path), name + '.h5')
            filenames.append(full_path)

            if os.path.exists(full_path):
                previous_df = pd.read_hdf(full_path, key='df')
                df = pd.concat([previous_df, df])
            df.to_hdf(full_path, key='df', mode='w')
            self.index_series.to_hdf(full_path, key='id')
            columns = pd.Series(df.columns)
            columns.to_hdf(full_path, key='col')

        return filenames