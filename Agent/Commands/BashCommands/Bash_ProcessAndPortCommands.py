#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class StopService(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        serviceName = self.request[0]
        return RunSubProcess(f"sudo service {serviceName} stop")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Stops a service with provided name.\n"
                           "       stopservice [ServiceName]\n"
                           "                     'ServiceName' - The name of the service being stopped")


class ReverseShell(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        path = self.request[0]

        return RunSubProcess(f"python import socket {path}")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "        reverseshell [path]"
                           "        Performs the bash command: 'python import socket [path]'\n"
                           "                path - the path for the reverse shell")


class KillProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        killType = self.request[0]
        killName = self.request[1]
        if killType == "-p":
            return RunSubProcess(f"sudo kill -9 $(lsof -t -i:{killName})")
        if killType == "-n":
            return RunSubProcess(f"sudo killall -9 {killName}")
        if killType == "-s":
            return RunSubProcess(f"sudo pkill -9 {killName}")
        if killType == "-i":
            return RunSubProcess(f"sudo kill -9 {killName}")
        return PrintRedAndLog(f"Invalid parameter killType: {killType} passed")

    def HelpRequested(self):
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
StopService.PublicFacing = "stopservice"
