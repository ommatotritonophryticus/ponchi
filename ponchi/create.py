from shutil import copy
from pathlib import Path


# Функиця копирования файлов из директрии с чистым проектом в текущую
def create() -> None:
    module_directory: Path = Path(__file__).parent
    for i in ['application.py', 'config.py']:
        copy(module_directory / 'clear_app' / i, '.')
