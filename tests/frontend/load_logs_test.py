import unittest
from src.frontend.load_logs import load_log, list_logs

class LoadLogsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.log_files = list_logs("tests/frontend/logs/")
        self.assertIsNotNone(self.log_files)

        expected = ['tests/frontend/logs/gpu-query.csv', 'tests/frontend/logs/k10temp-pci-00cb.csv', 'tests/frontend/logs/ath10k_hwmon-pci-0300.csv', 'tests/frontend/logs/asuswmisensors-isa-0000.csv', 'tests/frontend/logs/ram-query.csv', 'tests/frontend/logs/k10temp-pci-00c3.csv', 'tests/frontend/logs/cpu-query.csv']
        self.assertEquals(expected, self.log_files)

    def test_load_all(self):
        """Sanity checks that loading runs without error.
        """
        for log_file in self.log_files:
            self.assertIsNotNone(load_log(log_file))

if __name__ == "__main__":
    unittest.main()