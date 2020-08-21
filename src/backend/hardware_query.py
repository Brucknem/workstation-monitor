import shlex
import subprocess
import numpy as np
import pandas as pd
from datetime import datetime

timestamp_format = f'%Y/%m/%d %H:%M:%S.%f'


class HardwareQuery:
    """Base class for hardware queries.
    """

    def get_timestamp(self):
        """Get the current timestamp.
        """
        return datetime.now().strftime(timestamp_format)

    def get_bash_command(self) -> str:
        """The bash command used to query the hardware.
        """
        raise NotImplementedError('Implement the bash command')

    def get_default_dataframe(self) -> pd.DataFrame:
        """Get an empty default dataframe.
        """
        df = pd.DataFrame(data={'timestamp': [self.get_timestamp()]})
        df = df.set_index('timestamp')
        return df

    def get_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['timestamp']

    def parse_query_result(self, result: str) -> pd.DataFrame:
        """Parse the query result.
        """
        raise NotImplementedError('Implement the parsing')

    def query(self) -> pd.DataFrame:
        """Queries the hardware and creates a dataframe from it.
        """
        df = self.get_default_dataframe()
        try:
            process = subprocess.Popen(
                shlex.split(self.get_bash_command()),
                stdout=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                raise ValueError(error)
            df = self.parse_query_result(output.decode())
        except ValueError as e:
            print(e)
        df = df.set_index(self.get_index())
        return df


if __name__ == "__main__":
    query_gpu()
