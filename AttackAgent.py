#!/usr/bin/python3
import sys
from venv.AttackAgent.BaseCommands.CommandExecutor import RunCommands
from venv.AttackAgent.BaseCommands.CommandQueue import EnqueueCommand
from venv.AaSystem.AriotsShield import RunningOnPermittedMachine
from venv.AaSystem.Colors import PrintRed


def WaitForInput():
    if not RunningOnPermittedMachine():
        PrintRed("Not running on non Ariots permitted machine. Exiting")
        return
    print("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information")
    while True:
        userInput = input("\nPlease enter your next command, type help for options\n")
        EnqueueCommand(userInput)
        RunCommands()


if len(sys.argv) > 1:
    if RunningOnPermittedMachine():
        EnqueueCommand(" ".join(sys.argv[1:]))
        RunCommands()
    else:
        PrintRed("Not running on non Ariots permitted machine. Exiting")
elif __name__ == '__main__':
    WaitForInput()