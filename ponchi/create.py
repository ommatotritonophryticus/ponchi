from shutil import copy
from pathlib import Path


def create() -> None:
    """
    Copy files from clear_project to current directory
    """

    module_directory: Path = Path(__file__).parent
    for i in ['application.py', 'config.py']:
        copy(module_directory / 'clear_app' / i, '.')
