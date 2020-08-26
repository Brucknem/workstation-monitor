import os
from pathlib import Path

import pandas as pd


def read_from_hdf5(path: str, key: str):
    """
    Reads the given key from the hdf5 file.

    Args:
        path: The path to the hdf5 file
        key: The key to read

    Returns:
        The object that is written in the hdf5 file
    """
    if not path.endswith('.h5'):
        raise ValueError(f'Cannot load file {path}. Must be a .h5 file.')
    try:
        absolute = str(Path(os.path.expanduser(path)))
        value = pd.read_hdf(absolute, key=key, index=False)
        return value
    except FileNotFoundError:
        return None


def extract_names(log_files: list):
    """Returns the filename of the given log files.
    """
    return [str(log_file).split('/')[-1] for log_file in log_files]


def list_logs(path: str, extract=True):
    """Loads all logs in the given directory.

    Args:
        extract: Extract the filenames of the full paths and return these instead
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
