from importlib import machinery

config = machinery.SourceFileLoader('*', './config.py').load_module()
