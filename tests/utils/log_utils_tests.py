import shutil
import unittest
from pathlib import Path

from src.backend import MockQuery
from src.utils.log_utils import list_logs, read_from_hdf5


class LogUtilsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.output_path = str(Path('tests/utils/logs').absolute())
        Path(self.output_path).mkdir(parents=True, exist_ok=True)

        self.query = MockQuery()
        filenames = self.query.query_and_update(self.output_path)

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
        for log_file in self.log_files:
            df, indices, values = read_from_hdf5(log_file, 'df'), read_from_hdf5(log_file, 'id'), read_from_hdf5(
                log_file, 'val')
            self.assertCountEqual(indices, self.query.get_index())
            columns = list(indices)
            columns.extend(list(values))
            self.assertCountEqual(list(df.columns), columns)
            

if __name__ == "__main__":
    unittest.main()
