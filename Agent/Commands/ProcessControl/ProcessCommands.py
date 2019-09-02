#!/usr/bin/python3
from multiprocessing import Process
from AaSystem.Context.ContextFactory import GetContext
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


def InitQueueStartProcess(command):
    context = GetContext()
    context.CommandQueue.EnqueueCommand(command)
    context.CommandQueue.RunCommands()


class RunProcess(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        asyncCommand = ' '.join(self.request[0:])
        Process(target=InitQueueStartProcess, args=(asyncCommand,)).start()

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       Run async process help requested\n")


RunProcess.PublicFacing = "async"
