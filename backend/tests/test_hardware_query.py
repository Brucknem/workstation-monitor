import unittest

import pandas as pd

from backend import SensorsQuery, CPUQuery, GPUQuery, RAMQuery, MockQuery


class TestHardwareQuery(unittest.TestCase):
    """Test cases for the query GPU functions.
    """

    def assert_dataframe(self, names: list = None):
        """Asserts the common dataframe properties
        """
        all_index_names = ['timestamp']
        if names:
            all_index_names.extend(names)

        for name, frame in self.dfs.items():
            self.assert_index(all_index_names, frame)
            self.assert_timestamp_format(frame)

    def assert_timestamp_format(self, df: pd.DataFrame):
        """Asserts that the timestamps are all in the same format
        """
        timestamps = df['timestamp'].values
        self.assertEqual(timestamps.dtype, 'datetime64[ns]')

    def assert_index(self, names: list, df: pd.DataFrame):
        """Asserts that the index of the dataframe is the given list.
        """
        for name in names:
            self.assertIn(name, df.columns)

    def test_query_gpu(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.dfs = GPUQuery().query()
        self.assert_dataframe(['name', 'count'])

    def test_query_cpu(self):
        """Sanity checks that the CPU query produces a dataframe.
        """
        self.dfs = CPUQuery().query()
        self.assert_dataframe(['CPU'])

    def test_query_ram(self):
        """Sanity checks that the RAM query produces a dataframe.
        """
        self.dfs = RAMQuery().query()
        self.assert_dataframe(['type'])

    def test_query_sensors(self):
        """Sanity checks that the sensors query produces a dataframe.
        """
        self.dfs = SensorsQuery().query()
        self.assert_dataframe(['Adapter'])

    def test_query_mock(self):
        """Sanity checks that the mock query produces a dataframe.
        """
        self.dfs = MockQuery().query()
        self.assert_dataframe(['test'])


if __name__ == "__main__":
    unittest.main()
