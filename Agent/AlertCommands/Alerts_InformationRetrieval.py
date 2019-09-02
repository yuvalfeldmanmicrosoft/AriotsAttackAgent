#!/usr/bin/python3
from AaSystem.EventQueue.CommandQueue import EnqueueCommandsNext
from AaSystem.LogAndPrint.Log import PrintAndLog


def LinuxReconnaissance(request):
    if "-help" in request:
        Help_LinuxReconnaissance()
        return

    EnqueueCommandsNext(["custombash uname -n -s -r -v"])


def ClearHistoryFile(request):
    if "-help" in request:
        Help_ClearHistoryFile()
        return

    EnqueueCommandsNext(["custombash history -c"])


def Help_LinuxReconnaissance():
    return PrintAndLog("       Performs the bash command: 'uname -n -s -r -v'\n"
                       "       Triggers alert: 'LinuxReconnaissance'")


def Help_ClearHistoryFile():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'history -c'\n"
                       "       Triggers alert: 'ClearHistoryFile'")


LinuxReconnaissance.PublicFacing = "linuxreconnaissance"
ClearHistoryFile.PublicFacing = "clearhistoryfile"
