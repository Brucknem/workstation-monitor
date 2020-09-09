import unittest

import pandas as pd

from tests.backend.hardware_query_write_to_file_tests_base import \
    HardwareQueryWriteToFileTestsBase


class HardwareQueryWriteToH5FileTests(HardwareQueryWriteToFileTestsBase):
    """Test cases for the query GPU functions.
    """

    def assert_files(self):
        for _ in range(10):
            filenames = self.query.query_and_update(self.output_path)

        for file in filenames:
            df = pd.read_hdf(file, key='df')
            indices = list(pd.read_hdf(file, key='id'))
            values = list(pd.read_hdf(file, key='val'))
            self.assertCountEqual(indices, self.query.get_index())

            columns = indices
            columns.extend(values)
            self.assertCountEqual(columns, list(df.columns))


if __name__ == "__main__":
    unittest.main()
