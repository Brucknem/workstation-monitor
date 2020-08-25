import os
import shutil
import unittest
from pathlib import Path
from src.utils.search_utils import search_dirs
from src.backend.sensors_query import SensorsQuery


class SearchUtilsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.search_path = str(Path('tests/utils/test_dirs').absolute())

    def assert_listed(self, path: str, expected: list):
        found_dirs = search_dirs(path)
        self.assertCountEqual(found_dirs, expected)

    def test_search_in_existing(self):
        """Sanity checks that searching runs without error.
        """
        path = self.search_path
        expected = [
             '/home/brucknem/Repositories/workstation-monitor/tests/utils/test_dirs/inner_test_dir',
             '/home/brucknem/Repositories/workstation-monitor/tests/utils/test_dirs/other_inner_test_dir']
        self.assert_listed(path, expected)

        path = os.path.join(self.search_path, '')
        self.assert_listed(path, expected)

        path = os.path.join(self.search_path, 'asdf')
        self.assert_listed(path, expected)


if __name__ == "__main__":
    unittest.main()
