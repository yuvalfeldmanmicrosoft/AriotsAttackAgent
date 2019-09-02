#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class PerformCustomCommand(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        return RunSubProcess(' '.join(self.request))

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs a custom bash command passed as the parameter")


PerformCustomCommand.PublicFacing = "custombash"
