import pandas as pd

from backend import HardwareQuery


class MockQuery(HardwareQuery):
    """Mock query.
    """

    def get_custom_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['test']

    def query(self) -> dict:
        """Queries the hardware and creates a dataframe from it.
        """
        timestamp = self.get_timestamp()
        data = {'timestamp': [timestamp for i in range(10)],
                'test': [i for i in range(10)],
                'values': [f'{i}' for i in range(10)]}
        df = pd.DataFrame(data=data)

        dfs = {'mock': df}
        return dfs
