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
    return pd.read_csv(Path(path), delimiter=';')

def load_logs(path: str):
    """Loads all logs in the given directory.

    Args:
        path (str): The path to the directory

    Returns:
        list: A list of pandas data frames, one for each log
    """
    fs_path = Path(path)
    log_files = [str(p) for p in fs_path.iterdir() if p.is_file()]
    logs = {log_file: load_log(log_file) for log_file in log_files}
    return logs