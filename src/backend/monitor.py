import os
import argparse
from time import sleep
from pathlib import Path
import logging
from systemd.journal import JournaldLogHandler
from src.backend.sensors_query import SensorsQuery
from src.backend.gpu_query import GPUQuery
from src.backend.ram_query import RAMQuery
from src.backend.cpu_query import CPUQuery
from src.backend.hardware_query import HardwareQuery
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--output_dir",
                    help="The output dir to write the csvs to.")
args = parser.parse_args()
output_path = Path(
    os.path.expanduser(
        args.output_dir if args.output_dir else '~/workstation-monitor'))
output_path.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger('workstation-monitor')
journald_handler = JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(message)s'
))
logger.setLevel(logging.DEBUG)
logger.addHandler(journald_handler)

queries = [
    SensorsQuery(logger),
    GPUQuery(logger),
    RAMQuery(logger),
    CPUQuery(logger)
]

with ThreadPoolExecutor(max_workers=len(queries)) as executor:
    while True:
        try:
            futures = {executor.submit(query.query_and_update, output_path): query.get_subclass_name() for query in queries}
            for future in as_completed(futures):
                query = futures[future]
                try:
                    filenames = future.result()
                except Exception as exc:
                    logging.error(f'{query} generated an exception: {exc}')
                else:
                    for filename in filenames:
                        logging.info(f'Updated: {filename}')
        except KeyboardInterrupt:
            logger.info('Exiting monitor')
            break
        sleep(1)
