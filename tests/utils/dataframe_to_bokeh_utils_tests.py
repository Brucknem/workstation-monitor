import os
import shutil
import unittest
from pathlib import Path
from src.utils.log_utils import list_logs, load_log
from src.backend import MockQuery
from src.utils.dataframe_to_bokeh_utils import convert_dataframe_to_column_data_source, render_bokeh

class ConvertDataFrameToColumnDataSourceTests(unittest.TestCase):
    """Test cases for the load logs functions.
    """
    def setUp(self):
        """Setup
        """
        self.output_path = str(Path('tests/utils/logs').absolute())
        Path(self.output_path).mkdir(parents=True, exist_ok=True)

        self.query = MockQuery()
        for i in range(10):
            filenames = self.query.query_and_update(self.output_path)
        
        log_files = list_logs(self.output_path, extract=False)
        self.assertCountEqual(log_files, filenames)
        self.df, self.indices = load_log(log_files[0])

    def tearDown(self):
        """Teardown
        """
        shutil.rmtree(self.output_path, ignore_errors=True)
        

    def test_load_all(self):
        """Sanity checks that loading runs without error.
        """
        cds = convert_dataframe_to_column_data_source(self.df, self.indices)
    
    


if __name__ == "__main__":
    unittest.main()
