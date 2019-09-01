#!/usr/bin/python3
import os
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def PerformCustomCommand(request):
    if not request:
        PrintRedAndLog("Missing bash command")
    if "-help" in request:
        Help_PerformCustomCommand()
        return

    return RunSubProcess(request[0])


def Help_PerformCustomCommand():
    return PrintAndLog("\n"
                       "       Performs a custom bash command passed as the parameter")


PerformCustomCommand.PublicFacing = "custombash"
