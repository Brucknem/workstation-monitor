import os
import shutil
import unittest
import pandas as pd
from pathlib import Path
from src.backend import SensorsQuery, CPUQuery, GPUQuery, RAMQuery, MockQuery
from datetime import datetime
from tests.backend.hardware_query_write_to_file_tests_base import HardwareQueryWriteToFileTestsBase

class HardwareQueryWriteToJFileTests(HardwareQueryWriteToFileTestsBase):
    """Test cases for the query GPU functions.
    """
    
    def assert_files(self):
        for _ in range(10):
            filenames = self.query.query_and_update(self.output_path, 'json')

        for file in filenames:
            df = pd.read_json(file)

if __name__ == "__main__":
    unittest.main()
