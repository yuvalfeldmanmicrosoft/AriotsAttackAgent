#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class LinuxReconnaissance(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["custombash uname -n -s -r -v"])

    def HelpRequested(self):
        return PrintAndLog("       Performs the bash command: 'uname -n -s -r -v'\n"
                           "       Triggers alert: 'LinuxReconnaissance'")


class ClearHistoryFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["custombash history -c"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'history -c'\n"
                           "       Triggers alert: 'ClearHistoryFile'")


LinuxReconnaissance.PublicFacing = "linuxreconnaissance"
ClearHistoryFile.PublicFacing = "clearhistoryfile"
