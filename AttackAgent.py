#!/usr/bin/python3
import multiprocessing
import sys
from AaSystem.Context.ContextFactory import GetContext
from AaSystem.LogAndPrint.Log import PrintRedAndLog, PrintAndLog, WriteToLog
from AaSystem.OperatingSystem.AriotsShield import RunningOnPermittedMachine
from AaSystem.EndpointMap.EndpointMapper import CreatePublicEndpointMap

CreatePublicEndpointMap()


def EnqueueAndRun(request):
    context = GetContext()
    context.CommandQueue.EnqueueCommand(request)
    context.CommandQueue.RunCommands()


def WaitForInput():
    if not RunningOnPermittedMachine():
        PrintRedAndLog("Not running on non Ariots permitted machine. Exiting")
        return
    PrintAndLog("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information")
    while True:
        EnqueueAndRun(input("\nPlease enter your next command, type help for options\n"))


if len(sys.argv) > 1:
    if RunningOnPermittedMachine():
        WriteToLog(f"User input: {sys.argv}")
        EnqueueAndRun(" ".join(sys.argv[1:]))
    else:
        PrintRedAndLog("Not running on non Ariots permitted machine. Exiting")
elif __name__ == '__main__':
    WaitForInput()
