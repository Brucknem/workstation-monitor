import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path
from io import StringIO


def list_dirs(path: Path) -> list:
    """Lists all directories in the given path.
    """
    return [str(p) for p in path.iterdir()
            if not p.is_file()]


def search_dirs(path: str):
    """Loads all logs in the given directory.

    Args:
        path (str): The path to the directory

    Returns:
        list: A list of pandas data frames, one for each log
    """
    fs_path = Path(os.path.expanduser(path))
    if fs_path.exists():
        return list_dirs(fs_path)

    fs_path = fs_path.parent
    return list_dirs(fs_path)
