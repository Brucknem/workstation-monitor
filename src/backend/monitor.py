import os
import argparse
from pathlib import Path
from src.backend.sensors_query import SensorsQuery
from src.backend.gpu_query import GPUQuery
from src.backend.ram_query import RAMQuery
from src.backend.cpu_query import CPUQuery
from src.backend.hardware_query import HardwareQuery

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--output_dir", help="The output dir to write the csvs to.")
args = parser.parse_args()
output_path = Path(os.path.expanduser(args.output_dir if args.output_dir else '~/workstation-monitor'))
output_path.mkdir(parents=True, exist_ok=True)

# Query
SensorsQuery().query_and_update(output_path)
GPUQuery().query_and_update(output_path)
RAMQuery().query_and_update(output_path)
CPUQuery().query_and_update(output_path)