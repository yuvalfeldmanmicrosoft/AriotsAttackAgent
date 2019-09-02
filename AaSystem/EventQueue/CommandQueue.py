#!/usr/bin/python3
import queue
import shlex
from AaSystem.EndpointMap.EndpointMap import CommandMapping
from AaSystem.LogAndPrint.Log import PrintRedAndLog


class CommandQueue:
    def __init__(self):
        self.commandQueue = queue.Queue()
        self.tempQueue = queue.Queue()
        self.context = None

    def SetContext(self, context):
        self.context = context

    def CommandQueueNotEmpty(self):
        return not self.commandQueue.empty()

    def EnqueueCommand(self, command):
        commandClass = self.GetCommandClass(command)
        if commandClass:
            self.commandQueue.put(commandClass)

    def EnqueueCommands(self, commands):
        for command in commands:
            commandClass = self.GetCommandClass(command)
            if commandClass:
                self.commandQueue.put(commandClass)

    def EnqueueCommandsNext(self, commands):
        while not self.commandQueue.empty():
            self.tempQueue.put(self.commandQueue.get())
        for command in commands:
            commandClass = self.GetCommandClass(command)
            if commandClass:
                self.commandQueue.put(commandClass)
        while not self.tempQueue.empty():
            self.commandQueue.put(self.tempQueue.get())

    def DeQueueCommand(self):
        return self.commandQueue.get() if self.CommandQueueNotEmpty() else None

    def EmptyCommandQueue(self):
        while not self.commandQueue.empty():
            self.commandQueue.get()

    def GetCommandClass(self, request):
        if not request:
            PrintRedAndLog("Request cannot be null or empty")
            return None
        request = shlex.split(request)
        if len(request) < 1:
            PrintRedAndLog("")
            return None

        requestedCommand = str.lower(request[0])

        if requestedCommand not in CommandMapping:
            PrintRedAndLog(f"No such supported command '{requestedCommand}'")
            return None
        return CommandMapping[requestedCommand](request[1:], self.context)

    def RunCommands(self):
        while self.CommandQueueNotEmpty():
            command = self.DeQueueCommand()
            try:
                command.Execute()
            except Exception as ex:
                PrintRedAndLog(f"Failed command , exception encountered:\n\n        {ex}\n")
                self.EmptyCommandQueue()
                return

