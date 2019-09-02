#!/usr/bin/python3
from AaSystem.RequestManagment.PublicEndpointMap import CommandMapping
from AaSystem.LogAndPrint.Log import PrintRedAndLog
from AaSystem.EventQueue.CommandQueue import EmptyCommandQueue, DeQueueCommand, CommandQueueNotEmpty
from AaSystem.RequestManagment.RequestBuilder import ParseRequest
from Agent.BasicHelpers.BasicHelpCommands import BaseCommandsHelp


def RunCommand(request):
    if not request:
        PrintRedAndLog("Request cannot be null or empty")
        return False

    request = ParseRequest(request)

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
    return CommandMapping[requestedCommand](request[1:])


def RunCommands():
    while CommandQueueNotEmpty():
        request = DeQueueCommand()
        success = RunCommand(request)
        if success is not None and not success:
            EmptyCommandQueue()
            return

