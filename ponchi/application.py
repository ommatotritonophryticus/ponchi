from importlib import machinery
import logging

logger = logging.getLogger('ponchi.application')

logger.debug('Init application')
try:
    app = machinery.SourceFileLoader('*', './application.py').load_module()
except:
    logger.critical('Application import error. Check if application.py exists in the current directory.')
    exit()
