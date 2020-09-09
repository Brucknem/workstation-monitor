from typing import Dict

import numpy as np
import pandas as pd

from backend.hardware_query import HardwareQuery


class CPUQuery(HardwareQuery):
    """Query for the GPU.
    """

    def get_bash_command(self):
        """inherited
        """
        return "mpstat -P ALL"

    def get_custom_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['CPU']

    def parse_query_result(self, result) -> Dict[str, pd.DataFrame]:
        """inherited
        """
        lines = result.splitlines()[2:]
        lines = np.array(
            [np.array(line.split(), dtype=np.dtype(object)) for line in lines])
        lines = lines.transpose()
        lines[0] = [self.timestamp for i in range(len(lines[1]))]
        lines[0][0] = 'timestamp'
        data = {line[0]: line[1:] for line in lines}
        df = pd.DataFrame(data=data)

        return {'cpu': df}


if __name__ == "__main__":
    CPUQuery().query()
