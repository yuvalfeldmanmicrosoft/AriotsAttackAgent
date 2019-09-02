#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class ReverseShellAlert(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(f"reverseshell /bin/sh")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "        Performs the bash command python import socket /bin/sh\n"
                           "        Triggers alert: ReverseShell\n")


ReverseShellAlert.PublicFacing = "reverseshellalert"
