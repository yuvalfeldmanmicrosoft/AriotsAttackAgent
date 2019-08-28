#!/usr/bin/python3
from AaSystem.RequestManagment.CommandFileReferences import *
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from AaSystem.EventQueue.CommandQueue import EmptyCommandQueue, DeQueueCommand, CommandQueueNotEmpty
from AaSystem.RequestManagment.RequestBuilder import ParseRequest
from AaSystem.Reflection.Reflect import GetPublicFacingFunctionsFromPath


CommandMapping = {}


def CreateCommandConnections():
    for commandType in CommandTypes:
        if commandType not in CommandMapping:
            CommandMapping[commandType] = {}
        commands = GetPublicFacingFunctionsFromPath(CommandTypes[commandType])
        for command in commands:
            CommandMapping[str.lower(commandType)][str.lower(command[1].PublicFacing)] = command[1]


def RunCommand(request):
    if not request:
        PrintRedAndLog("Request cannot be null or empty")
        return False
    request = ParseRequest(request)

    if len(request) < 2:
        PrintRedAndLog("Request Missing parameters")
        return False
    requestedCommandType = str.lower(request[0])
    requestedCommand = str.lower(request[1])

    return CommandMapping[requestedCommandType][requestedCommand](request[2:])


def RunCommands():
    while CommandQueueNotEmpty():
        request = DeQueueCommand()
        success = RunCommand(request)
        if not success:
            EmptyCommandQueue()
            return


def HelpRequested():
    PrintAndLog("All commands follow the format - [CommandType] [CommandsParameter] [CommandsParameter] ...\n"
                "Type -help with any CommandType for more information on that command\n\n"
                "Available CommandsTypes:\n"
                "ba: Bash Attacks using bash commands to perform tasks\n"
                "run: References text files containing a row delimited list of commands to run, "
                "places these commands at "
                "the front of the queue\n"
                "sc: Attack Agent System Commands - will perform program and environment commands "
                "such as waiting, looping, "
                "handling environment variables and so on\n"
                "upgrade: Upgrades to latest version of Ariots Attack Agent - currently only "
                "supported on linux machines")
