#!/usr/bin/python3
import queue
import shlex
from AaSystem.EndpointMap.EndpointMap import CommandMapping
from AaSystem.LogAndPrint.Log import PrintRedAndLog
from Agent.BasicHelpers.BasicHelpCommands import BaseCommandsHelp


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
        self.commandQueue.put(command)

    def EnqueueCommands(self, commands):
        for command in commands:
            self.commandQueue.put(command)

    def EnqueueCommandsNext(self, commands):
        while not self.commandQueue.empty():
            self.tempQueue.put(self.commandQueue.get())
        for command in commands:
            self.commandQueue.put(command)
        while not self.tempQueue.empty():
            self.commandQueue.put(self.tempQueue.get())

    def DeQueueCommand(self):
        return self.commandQueue.get() if self.CommandQueueNotEmpty() else None

    def EmptyCommandQueue(self):
        while not self.commandQueue.empty():
            self.commandQueue.get()

    def RunCommand(self, request):
        if not request:
            PrintRedAndLog("Request cannot be null or empty")
            return False

        request = shlex.split(request)

        if len(request) < 1:
            PrintRedAndLog("Request Missing parameters")
            return False
        requestedCommand = str.lower(request[0])
        if requestedCommand == "-help":
            BaseCommandsHelp()
            return True
        if requestedCommand not in CommandMapping:
            PrintRedAndLog(f"No such supported command '{requestedCommand}'")
            return False
        return CommandMapping[requestedCommand](request[1:], self.context)

    def RunCommands(self):
        while self.CommandQueueNotEmpty():
            request = self.DeQueueCommand()
            success = self.RunCommand(request)
            if success is not None and not success:
                self.EmptyCommandQueue()
                return
