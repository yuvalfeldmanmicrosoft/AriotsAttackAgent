#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class RunProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        print("running!")

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       StopProcess help requested\n")


class StopProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        print("stopping!")

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       StopProcess help requested\n")


class GetProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        print("getting!")

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       GetProcess help requested\n")


class WaitForProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        print("waiting!")

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       WaitForProcess help requested\n")


RunProcess.PublicFacing = "runProcess"
StopProcess.PublicFacing = "stopProcess"
GetProcess.PublicFacing = "getProcess"
WaitForProcess.PublicFacing = "waitProcess"
