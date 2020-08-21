from src.backend.hardware_query import HardwareQuery
import pandas as pd
import numpy as np


class CPUQuery(HardwareQuery):
    """Query for the GPU.
    """

    def get_bash_command(self):
        """inherited
        """
        return "mpstat -P ALL"

    def get_default_dataframe(self) -> pd.DataFrame:
        """Get an empty default dataframe.
        """
        df = pd.DataFrame(data={
            'timestamp': [self.get_timestamp()],
            'CPU': [None]
        })
        return df

    def get_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['timestamp', 'CPU']

    def parse_query_result(self, result) -> pd.DataFrame:
        """inherited
        """
        lines = result.splitlines()[2:]
        lines = np.array(
            [np.array(line.split(), dtype=np.dtype(object)) for line in lines])
        lines = lines.transpose()
        timestamp = self.get_timestamp()
        lines[0] = [timestamp for i in range(len(lines[1]))]
        lines[0][0] = 'timestamp'
        data = {line[0]: line[1:] for line in lines}
        df = pd.DataFrame(data=data)

        return df


if __name__ == "__main__":
    CPUQuery().query()
