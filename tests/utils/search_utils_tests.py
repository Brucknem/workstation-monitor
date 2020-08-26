import os
import shutil
import unittest
from pathlib import Path
from src.utils.search_utils import search_dirs

class SearchUtilsTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """

    def setUp(self):
        """Setup
        """
        self.search_path = 'tests/utils/test_dir'

    def assert_listed(self, path: str, expected: list):
        found_dirs = search_dirs(path)
        self.assertCountEqual(found_dirs, expected)

    def test_search_in_existing(self):
        """Sanity checks that searching runs without error.
        """
        path = self.search_path
        expected = [
             'tests/utils/test_dir/inner_test_dir',
             'tests/utils/test_dir/other_inner_test_dir']
        self.assert_listed(path, expected)

        path = os.path.join(self.search_path, '')
        self.assert_listed(path, expected)

        path = os.path.join(self.search_path, 'asdf')
        self.assert_listed(path, expected)


if __name__ == "__main__":
    unittest.main()
