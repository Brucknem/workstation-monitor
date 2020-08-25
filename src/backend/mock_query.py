from src.backend.hardware_query import HardwareQuery
import pandas as pd
import numpy as np


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
        data = {
            'timestamp': [self.get_timestamp() for i in range(10)],
            'test': [i for i in range(10)],
            'values': [i for i in range(10)]
        }
        df = pd.DataFrame(data=data)
        df = df.set_index(self.get_index())

        dfs = { 'mock': df}
        return dfs


if __name__ == "__main__":
    CPUQuery().query()
