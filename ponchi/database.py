from importlib import import_module
from .config import config

DB = import_module(config.DATABASE['type']).DB(config.DATABASE)
