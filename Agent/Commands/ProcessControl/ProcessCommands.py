#!/usr/bin/python3
import multiprocessing
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
                    "       Async creates a new process and runs a provided command on that process. The "
                    "provided command can be a scenario command\n"
                    "       async [command]\n"
                    "               'command' - The command that will be run in a new process\n")


class RunProcessPool(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        poolSize = self.request[0]
        asyncCommands = self.request[1:]
        p = multiprocessing.Pool(int(poolSize))
        p.map(InitQueueStartProcess, asyncCommands)

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       Asyncpool creates a new process and runs a provided command on that process.\n"
                    "       The "
                    "provided command can be a scenario command\n"
                    "       async [poolSize] [command] [command] [command]\n"
                    "               'poolSize' -    The number of processes that will be opened for the commands\n"
                    "               'command' -     The command that will be run in a new process. It is important "
                    "that all commands be enveloped in brackets to separate commands\n")


RunProcess.PublicFacing = "async"
RunProcessPool.PublicFacing = "asyncpool"
