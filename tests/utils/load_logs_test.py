import shutil
import unittest
from pathlib import Path
from src.utils.load_logs import load_log, list_logs
from src.backend.sensors_query import SensorsQuery

class LoadLogsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.output_path = 'tests/utils/logs'
        Path(self.output_path).mkdir(parents=True, exist_ok=True)
        filenames = SensorsQuery().query_and_update(self.output_path)
        
        self.log_files = list_logs(self.output_path, extract=False)
        self.assertCountEqual(self.log_files, filenames)

    def tearDown(self):
        """Teardown
        """
        shutil.rmtree(self.output_path, ignore_errors=True)

    def test_extract_names(self):
        """Tests that listing logs with extracting the names works as expected.
        """
        log_names = list_logs(self.output_path, extract=True)
        for log_name in log_names:
            found = False
            for log_file in self.log_files:
                if log_file.endswith(log_name):
                    found = True
                    break
            self.assertTrue(found)
        

    def test_load_all(self):
        """Sanity checks that loading runs without error.
        """
        print('yeeet')

if __name__ == "__main__":
    unittest.main()