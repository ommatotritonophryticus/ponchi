from importlib import machinery

app = machinery.SourceFileLoader('*', './application.py').load_module()
