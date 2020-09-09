import unittest

import pandas as pd

from backend.tests import HardwareQueryWriteToFileTestsBase


class TestHardwareQueryWriteToJsonFile(HardwareQueryWriteToFileTestsBase):
    """Test cases for the query GPU functions.
    """

    def assert_files(self):
        if not self.query:
            return
        
        for _ in range(10):
            filenames = self.query.query_and_update(self.output_path, 'json')

        for file in filenames:
            pd.read_json(file)


if __name__ == "__main__":
    unittest.main()
