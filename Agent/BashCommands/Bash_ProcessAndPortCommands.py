#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def ReverseShell(request):
    if "-help" in request:
        Help_ReverseShell()
        return

    return RunSubProcess("python import socket /bin/sh")


def KillProcess(request):
    if "-help" in request:
        Help_KillProcess(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
    killType = request[0]
    killName = request[1]
    if killType == "-p":
        return RunSubProcess(f"sudo kill -9 $(lsof -t -i:{killName})")
    if killType == "-n":
        return RunSubProcess(f"sudo killall -9 {killName}")
    if killType == "-s":
        return RunSubProcess(f"sudo pkill -9 {killName}")
    if killType == "-i":
        return RunSubProcess(f"sudo kill -9 {killName}")
    return PrintRedAndLog(f"Invalid parameter killType: {killType} passed")


def Help_ReverseShell():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'python import socket /bin/sh'\n"
                       "       Triggers alert: 'ReverseShell'")



def Help_KillProcess(request):
    return PrintAndLog("\n"
                       "       Kills an active process\n"
                       "       killprocess [KillType] [KillName]\n"
                       "                     'KillType' - the type of parameter that will be passed in the KillName, "
                       "currently supporting:\n"
                       "                     '-p' - KillName is a port and the process on that port will be "
                       "terminated\n"
                       "                     '-n' - KillName is an exact process name and that process will be "
                       "terminated\n"
                       "                     '-s' - KillName is a partial name and all processes containing KillName"
                       " will be terminated\n"
                       "                     '-i' - KillName is a PID (Process ID) and a process with that PID "
                       "will be terminated\n"
                       "                     'KillName' - The name of the parameter that will be killed according "
                       "the KillType")


ReverseShell.PublicFacing = "reverseshell"
KillProcess.PublicFacing = "killprocess"
