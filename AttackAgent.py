#!/usr/bin/python3
import sys

from Agent.AaSystem.AriotsShield import RunningOnPermittedMachine
from Agent.AaSystem.Log import PrintRedAndLog, PrintAndLog, WriteToLog
from Agent.AttackAgent.BaseCommands.CommandExecutor import RunCommands
from Agent.AttackAgent.BaseCommands.CommandQueue import EnqueueCommand


def WaitForInput():
    if not RunningOnPermittedMachine():
        PrintRedAndLog("Not running on non Ariots permitted machine. Exiting")
        return
    PrintAndLog("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information")
    while True:
        userInput = input("\nPlease enter your next command, type help for options\n")
        WriteToLog(f"User input: {userInput}")
        EnqueueCommand(userInput)
        RunCommands()


if len(sys.argv) > 1:
    if RunningOnPermittedMachine():
        WriteToLog(f"User input: {sys.argv}")
        EnqueueCommand(" ".join(sys.argv[1:]))
        RunCommands()
    else:
        PrintRedAndLog("Not running on non Ariots permitted machine. Exiting")
elif __name__ == '__main__':
    WaitForInput()