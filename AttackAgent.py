import sys
from venv.BaseCommandHandling.CommandQueue import EnqueueCommand
from venv.BaseCommandHandling.CommandExecutor import RunCommands


def WaitForInput():
    print("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information")
    while True:
        userInput = input("\nPlease enter your next command, type help for options\n")
        EnqueueCommand(userInput)
        RunCommands()


if len(sys.argv) > 1:
    EnqueueCommand(" ".join(sys.argv[1:]))
    RunCommands()
elif __name__ == '__main__':
    WaitForInput()