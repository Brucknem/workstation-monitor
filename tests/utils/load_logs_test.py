import unittest
from src.utils.load_logs import load_log, list_logs

class LoadLogsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.log_files = list_logs("tests/utils/logs/", extract=False)
        self.assertIsNotNone(self.log_files)

        expected = ['tests/utils/logs/gpu-query.csv', 'tests/utils/logs/k10temp-pci-00cb.csv', 'tests/utils/logs/ath10k_hwmon-pci-0300.csv', 'tests/utils/logs/asuswmisensors-isa-0000.csv', 'tests/utils/logs/ram-query.csv', 'tests/utils/logs/k10temp-pci-00c3.csv', 'tests/utils/logs/cpu-query.csv']
        self.assertEqual(len(expected), len(self.log_files))
        for name in expected:
            self.assertIn(name, self.log_files)

    def test_load_all(self):
        """Sanity checks that loading runs without error.
        """
        for log_file in self.log_files:
            self.assertIsNotNone(load_log(log_file))

if __name__ == "__main__":
    unittest.main()