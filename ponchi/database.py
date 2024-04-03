from importlib import import_module
from .config import config
import logging

logger = logging.getLogger('ponchi.database')

logger.debug('Init database')
try:
    DB = import_module(config.DATABASE['type']).DB(config.DATABASE)
except:
    logger.critical('Configuration import error. Check if config.py exists in the current directory.')
    exit()