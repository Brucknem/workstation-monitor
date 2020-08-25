import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path
from io import StringIO


def load_log(path: str):
    """Loads one given log file.

    Args:
        path (str): The path to the log file

    Raises:
        ValueError: Raised if path is not a .csv file

    Returns:
        DataFrame: A pandas data frame.
    """
    if not path.endswith('.h5'):
        raise ValueError(f'Cannot load file {path}. Must be a .h5 file.')
    try:
        absolute = str(Path(os.path.expanduser(path)))
        df = pd.read_hdf(absolute, key='df')
        indices = list(pd.read_hdf(absolute, key='id'))
        return df, indices
    except FileNotFoundError:
        return None, []

def extract_names(log_files: list):
    """Returns the filename of the given log files.
    """
    return [str(log_file).split('/')[-1] for log_file in log_files]


def list_logs(path: str, extract=True):
    """Loads all logs in the given directory.

    Args:
        path (str): The path to the directory

    Returns:
        list: A list of pandas data frames, one for each log
    """
    fs_path = Path(os.path.expanduser(path))
    try:
        log_files = [
            str(p) for p in fs_path.iterdir()
            if p.is_file() and str(p).endswith('.h5')]
        if extract:
            return extract_names(log_files)
        else:
            return log_files
    except FileNotFoundError:
        return []
