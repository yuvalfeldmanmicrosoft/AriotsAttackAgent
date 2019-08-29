#!/usr/bin/python3
from AaSystem.RequestManagment.CommandFileReferences import *
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from AaSystem.EventQueue.CommandQueue import EmptyCommandQueue, DeQueueCommand, CommandQueueNotEmpty
from AaSystem.RequestManagment.RequestBuilder import ParseRequest
from AaSystem.Reflection.Reflect import GetPublicFacingFunctionsFromPath


CommandMapping = {}
CommandMappingNameByTree = {}


def CreateCommandConnections():
    for commandType in CommandTypes:
        if commandType not in CommandMappingNameByTree:
            CommandMappingNameByTree[commandType] = []
        for commandPath in CommandTypes[commandType]:
            commands = GetPublicFacingFunctionsFromPath(commandPath)
            for command in commands:
                CommandMapping[str.lower(command[1].PublicFacing)] = command[1]
                CommandMappingNameByTree[commandType].append(command[0])


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
        if not success:
            EmptyCommandQueue()
            return


def BaseCommandsHelp():
    PrintAndLog("\n"
                "       All commands follow the format - [CommandName] [CommandsParameter] [CommandsParameter] ...\n"
                "       Type -help with any CommandType for more information on that command\n\n"
                "       Available commands types:\n"
                "               Bash                Uses bash commands to perform tasks\n"
                "               Scenarios           References text files containing a row delimited list of commands "
                "to run, places these commands at the front of the queue\n"
                "               System              Perform program and environment commands such as waiting, "
                "looping, handling environment variables and so on\n"
                "               Upgrade             Upgrades to latest version of Ariots Attack Agent - currently only "
                "supported on linux machines\n\n"
                "       Type -help with a command type of the listed commands to get a list of available commands for"
                "that command type")


def BashCommandList(request):
    if "-help" not in request:
        return
    freeText = "       Uses bash commands to perform tasks"
    printHelpInfo(freeText, "bc")


def ScenariosCommandList(request):
    if "-help" not in request:
        return
    freeText = "       References text files containing a row delimited list of commands " \
               "to run, places these commands at the front of the queue"
    printHelpInfo(freeText, "run")


def SystemCommandList(request):
    if "-help" not in request:
        return
    freeText = "       Perform program and environment commands such as waiting, " \
               "looping, handling environment variables and so on"
    printHelpInfo(freeText, "sc")


def printHelpInfo(freeText, commandTree):
    text = f"{freeText}\n" \
           "       The available commands under this category are:\n\n"
    for command in CommandMappingNameByTree[commandTree]:
        text = f"{text}" \
               f"               {command}\n"
    text = f"{text}\n" \
           f"       Type -help with a command type of the listed commands to get additional information on that command"
    PrintAndLog(text)


BashCommandList.PublicFacing = "Bash"
ScenariosCommandList.PublicFacing = "Scenarios"
SystemCommandList.PublicFacing = "System"
