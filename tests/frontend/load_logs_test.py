import unittest
from src.frontend.load_logs import load_logs

class LoadLogsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def test_load_all(self):
        """Sanity checks that loading runs without error.
        """
        logs = load_logs("tests/frontend/logs/")
        assert logs

if __name__ == "__main__":
    unittest.main()