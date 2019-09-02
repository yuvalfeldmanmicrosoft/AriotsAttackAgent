#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def StopService(request, context):
    if "-help" in request:
        Help_StopService()
        return

    if not request or len(request) < 1:
        PrintRedAndLog("Missing required parameters")
        return

    serviceName = request[0]
    return RunSubProcess(f"sudo service {serviceName} stop")


def ReverseShell(request, context):
    if "-help" in request:
        Help_ReverseShell()
        return

    if not request or len(request) < 1:
        PrintRedAndLog("Missing required parameters")

    path = request[0]

    return RunSubProcess(f"python import socket {path}")


def KillProcess(request, context):
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
                       "        reverseshell [path]"
                       "        Performs the bash command: 'python import socket [path]'\n"
                       "                path - the path for the reverse shell")


def Help_KillProcess():
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


def Help_StopService():
    return PrintAndLog("\n"
                       "       Stops a service with provided name.\n"
                       "       stopservice [ServiceName]\n"
                       "                     'ServiceName' - The name of the service being stopped")


ReverseShell.PublicFacing = "reverseshell"
KillProcess.PublicFacing = "killprocess"
StopService.PublicFacing = "stopservice"
