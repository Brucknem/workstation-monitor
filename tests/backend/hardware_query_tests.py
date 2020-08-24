import unittest
from src.backend.gpu_query import GPUQuery
from src.backend.cpu_query import CPUQuery
from src.backend.ram_query import RAMQuery
from datetime import datetime


class HardwareQueryTests(unittest.TestCase):
    """Test cases for the query GPU functions.
    """

    def assert_dataframe(self, names: list = None):
        """Asserts the common dataframe properties
        """
        all_index_names = ['timestamp']
        if names:
            all_index_names.extend(names)
        self.assert_index(all_index_names)
        self.assert_timestamp_format()

    def assert_timestamp_format(self):
        """Asserts that the timestamps are all in the same format
        """
        indices = self.df.index.values
        if type(indices[0]) is not tuple:
            indices = [indices]

        for index in indices:
            datetime.fromisoformat(index[0].replace('Z', '+00:00'))


    def assert_index(self, names: list):
        """Asserts that the index of the dataframe is the given list.
        """
        index_names = self.df.index.names
        self.assertEqual(len(names), len(index_names))
        for name in names:
            self.assertIn(name, index_names)

    def test_query_gpu(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.df = GPUQuery().query()
        self.assert_dataframe()

    def test_query_cpu(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.df = CPUQuery().query()
        self.assert_dataframe(['CPU'])

    def test_query_ram(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.df = RAMQuery().query()
        self.assert_dataframe(['type'])


if __name__ == "__main__":
    unittest.main()
