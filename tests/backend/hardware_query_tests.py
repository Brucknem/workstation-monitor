import unittest
from src.backend.gpu_query import GPUQuery
from src.backend.cpu_query import CPUQuery


class HardwareQueryTests(unittest.TestCase):
    """Test cases for the query GPU functions.
    """

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
        self.assert_index(['timestamp'])

    def test_query_cpu(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.df = CPUQuery().query()
        self.assert_index(['CPU', 'timestamp'])


if __name__ == "__main__":
    unittest.main()
