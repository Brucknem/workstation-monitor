from typing import Dict

import pandas as pd

from backend import HardwareQuery
from backend.hardware_query import get_timestamp


class MockQuery(HardwareQuery):
    """Mock query.
    """

    def parse_query_result(self, result: str) -> pd.DataFrame:
        pass

    def get_bash_command(self) -> str:
        pass

    def get_custom_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['test']

    def query(self) -> Dict[str, pd.DataFrame]:
        """Queries the hardware and creates a dataframe from it.
        """
        timestamp = get_timestamp()
        data = {'timestamp': [timestamp for i in range(10)],
                'test': [i for i in range(10)],
                'values': [f'{i}' for i in range(10)]}
        df = pd.DataFrame(data=data)

        dfs = {'mock': df}
        return dfs
