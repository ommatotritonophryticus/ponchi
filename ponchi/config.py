from importlib import machinery
import logging

logger = logging.getLogger('ponchi.config')

logger.debug('Init config')
try:
    config = machinery.SourceFileLoader('*', './config.py').load_module()
except:
    logger.critical('Database initialization error check DATABASE parameter in config.py')
    exit()
