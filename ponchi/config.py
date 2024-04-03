"""
Config module
Imports the contents of ./config.py into the config variable
"""
import sys
from importlib import machinery
import logging

logger = logging.getLogger('ponchi.config')

logger.debug('Init config')
try:
    config = machinery.SourceFileLoader('*', './config.py').load_module()
except:
    logger.critical(
        'Configuration import error. Check if config.py exists in the current directory.'
    )
    sys.exit(1)
