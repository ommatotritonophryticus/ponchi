from ponchi.create import create
from sys import argv


def print_help():
    print("""Type "python3 -m ponchi createapp" to create clear application in current directory
"python3 -m ponchi start" to start bot
""")


if len(argv) < 2:
    argv.append(None)

if argv[1] == "createapp":
    print("Creating app...")
    create()
    print("Complite.")

elif argv[1] == "start":
    import ponchi.bot

elif argv[1] == "help":
    print_help()

else:
    print('Error. Type argument "help"')
