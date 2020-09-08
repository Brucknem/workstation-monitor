import os
import shutil
import unittest
import pandas as pd
from pathlib import Path
from src.backend import SensorsQuery, CPUQuery, GPUQuery, RAMQuery, MockQuery
from datetime import datetime

class HardwareQueryWriteToFileTestsBase(unittest.TestCase):
    """Test cases for the query GPU functions.
    """

    def assert_files(self):
        pass

    def tearDown(self):
        """Teardown
        """
        self.output_path = 'tests/backend/logs'
        shutil.rmtree(self.output_path, ignore_errors=True)

        Path(self.output_path).mkdir(parents=True, exist_ok=True)

        self.assert_files()

        shutil.rmtree(self.output_path, ignore_errors=True)

    def test_query_gpu(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.query = GPUQuery()

    def test_query_cpu(self):
        """Sanity checks that the CPU query produces a dataframe.
        """
        self.query = CPUQuery()

    def test_query_ram(self):
        """Sanity checks that the RAM query produces a dataframe.
        """
        self.query = RAMQuery()

    def test_query_sensors(self):
        """Sanity checks that the GPU query produces a dataframe.
        """
        self.query = SensorsQuery()

if __name__ == "__main__":
    unittest.main()