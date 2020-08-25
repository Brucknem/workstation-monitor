import os
import shutil
import unittest
import pandas as pd
from pathlib import Path
from src.backend.gpu_query import GPUQuery
from src.backend.cpu_query import CPUQuery
from src.backend.ram_query import RAMQuery
from src.backend.sensors_query import SensorsQuery
from datetime import datetime

class HardwareQueryWriteToFileTests(unittest.TestCase):
    """Test cases for the query GPU functions.
    """
    
    def tearDown(self):
        """Teardown
        """
        output_path = 'tests/backend/logs'
        Path(output_path).mkdir(parents=True, exist_ok=True)
        filenames = self.query.query_and_update(output_path)
        for file in filenames:
            df = pd.read_hdf(file, key='df')
            indices = list(pd.read_hdf(file, key='id'))
            self.assertCountEqual(indices, self.query.get_index())
            
            df_indices = df.index.names
            self.assertCountEqual(indices, df_indices)
        shutil.rmtree(output_path, ignore_errors=True)

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
