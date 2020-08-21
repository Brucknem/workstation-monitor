import unittest
from src.backend.query_gpu import query_gpu

class QueryGpuTests(unittest.TestCase):
    """Test cases for the query GPU functions.
    """

    def test_verify_dataframe(self):
        """Sanity checks that the query produces a dataframe.
        """
        df = query_gpu()
        self.assertEqual('timestamp', df.index.name)

if __name__ == "__main__":
    unittest.main()