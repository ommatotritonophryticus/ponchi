"""
Application entry point
"""
from sys import argv

from ponchi.create import create


def print_help():
    """
    Print help function
    """
    print("""Type "python3 -m ponchi createapp" to create clear application in current directory
"python3 -m ponchi start" to start bot
""")


if len(argv) < 2:
    argv.append("")

if argv[1] == "createapp":
    print("Creating app...")
    create()
    print("Complete.")

elif argv[1] == "start":
    import importlib
    import logging
    from ponchi.config import config
    logging.basicConfig(**config.LOG_CONFIG)
    log = logging.getLogger('ponchi_init')
    log.info('Ponchi start init')
    importlib.import_module("ponchi.bot")

elif argv[1] == "help":
    print_help()

else:
    print('Error. Type argument "help"')
