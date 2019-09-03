#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from AaSystem.OperatingSystem.SystemInspector import GetOperatingSystemName
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class IpConfig(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if str.lower(GetOperatingSystemName()) == "linux":
            return RunSubProcess("ifconfig -a")
        return RunSubProcess("ipconfig")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'ipconfig'\n"
                           "       Meant as a simple code functionality and sanity test")


class WhoAmI(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.request and self.request[0] == "-r":
            return RunSubProcess("sudo whoami")
        return RunSubProcess("whoami")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Runs the self discovering command 'whoami'\n"
                           "       The parameter -r can be passed at the end to indicate to run as root (sudo)")


class Ping(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(0):
            return
        requestPing = self.request[0]
        if requestPing == "google":
            return RunSubProcess("ping -c 4 google.com")
        if requestPing == "self":
            return RunSubProcess("ping -c 4 127.0.0.1")
        if requestPing == "8":
            return RunSubProcess("ping -c 4 8.8.8.8")
        if requestPing == "-c" and len(self.request) > 1:
            return RunSubProcess(f"ping -c 4 {self.request[1]}")
        PrintRedAndLog("Invalid or missing parameters")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       pings a destination url'\n"
                           "       Receives one of the following parameters:\n"
                           "                     'google' - pings google.com\n"
                           "                     'self' - pings 127.0.0.1\n"
                           "                     '8' - pings 8.8.8.8\n"
                           "                     '-c' - in this case the request takes in an additional parameter "
                           "[url] and pings that url - ping [url]\n"
                           "       The destination is pinged 4 times, the response will appear once all four "
                           "pings have completed")


IpConfig.PublicFacing = "getip"
WhoAmI.PublicFacing = "whoami"
Ping.PublicFacing = "ping"
