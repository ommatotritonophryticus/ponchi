"""
Contains an imported Database object dependent on the configuration
"""
from importlib import import_module
import logging
import sys

from ponchi.databases.db_interface import DBInterface
from .config import config

logger = logging.getLogger('ponchi.database')

logger.debug('Init database')
try:
    database: DBInterface = import_module(config.DATABASE['type']).Database(config.DATABASE)
except:
    logger.critical('Database initialization error check DATABASE parameter in config.py')
    sys.exit(1)
