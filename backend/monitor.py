import argparse
import logging
import os
from pathlib import Path
from time import sleep

from systemd.journal import JournaldLogHandler

from backend import SensorsQuery, CPUQuery, GPUQuery, RAMQuery
# Initiate the parser
from backend.gpu_query import has_gpu

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--output_dir",
                    help="The output dir to write the csvs to.")
args = parser.parse_args()
output_path = Path(os.path.expanduser(
    args.output_dir if args.output_dir else '~/workstation-monitor'))
output_path.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger('workstation-monitor')
journald_handler = JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.setLevel(logging.DEBUG)
logger.addHandler(journald_handler)

queries = [SensorsQuery(logger), RAMQuery(logger), CPUQuery(logger)]

if has_gpu():
    queries.append(GPUQuery(logger))
else:
    fdsadfsd
    
while True:
    try:
        for query in queries:
            query.query_and_update(output_path)
        sleep(1)
    except KeyboardInterrupt:
        logger.info('Exiting monitor')
        break
