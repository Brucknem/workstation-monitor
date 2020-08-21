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
        data = {'timestamp': [self.get_timestamp()]}
        for key in self.get_custom_index():
            data[key] = [None]
        df = pd.DataFrame(data=data)
        df = df.set_index(self.get_index())
        return df

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

    def query(self) -> pd.DataFrame:
        """Queries the hardware and creates a dataframe from it.
        """
        df = self.get_default_dataframe()
        try:
            process = subprocess.run(
                shlex.split(self.get_bash_command()), capture_output=True ,check=True)
            output, error = process.stdout, process.stderr
            if error:
                raise FileNotFoundError(error)
            df = self.parse_query_result(output.decode())
        except FileNotFoundError as e:
            print(e)
        except subprocess.CalledProcessError as e:
            print(e.output)
        
        df = df.set_index(self.get_index())
        return df


if __name__ == "__main__":
    query_gpu()
