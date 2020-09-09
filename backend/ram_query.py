from typing import Dict

import numpy as np
import pandas as pd

from backend import HardwareQuery


class RAMQuery(HardwareQuery):
    """Query for the GPU.
    """

    def get_bash_command(self):
        """inherited
        """
        return "free -wm"

    def get_custom_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['type']

    def parse_query_result(self, result) -> Dict[str, pd.DataFrame]:
        """inherited
        """
        lines = result.splitlines()
        lines = [np.array(line.split(), dtype=np.dtype(object)) for line in
                 lines]
        lines[0] = np.insert(lines[0], 0, 'type')
        lines[-1] = np.append(lines[-1],
                              [str(np.NaN)] * (len(lines[0]) - len(lines[-1])))
        lines = np.transpose(np.array(lines))

        data = {line[0]: line[1:] for line in lines}
        data['timestamp'] = [self.timestamp for _ in
                             range(len(data[list(data.keys())[0]]))]
        df = pd.DataFrame(data=data)

        return {'ram': df}


if __name__ == "__main__":
    RAMQuery().query()
