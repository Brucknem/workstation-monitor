import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path


def load_log(path: str):
    """Loads one given log file.

    Args:
        path (str): The path to the log file

    Raises:
        ValueError: Raised if path is not a .csv file

    Returns:
        DataFrame: A pandas data frame.
    """
    if not path.endswith('.csv'):
        raise ValueError(f'Cannot load file {path}. Must be a .csv file.')
    try:
        return pd.read_csv(Path(path), delimiter=';')
    except FileNotFoundError:
        return None

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
            if p.is_file() and str(p).endswith('.csv')]
        if extract:
            return extract_names(log_files)
        else:
            return log_files
    except FileNotFoundError:
        return []

def list_dirs(path: str):
    """Loads all logs in the given directory.

    Args:
        path (str): The path to the directory

    Returns:
        list: A list of pandas data frames, one for each log
    """
    split = path.rsplit('/', 1)
    corrected_path = ""
    if not split[0]:
        corrected_path = '/'
    else:
        corrected_path = split[0]

    fs_path = Path(corrected_path)
    try:
        log_files = [
            str(p) for p in fs_path.iterdir()
            if not p.is_file()]
        return log_files
    except FileNotFoundError:
        return []
