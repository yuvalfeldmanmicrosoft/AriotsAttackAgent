#!/usr/bin/python3
from Agent.AaSystem.Log import PrintAndLog, PrintBlueAndLog, PrintRedAndLog
from Agent.AttackAgent.BaseCommands import CommandQueueNotEmpty, DeQueueCommand, EmptyCommandQueue
from Agent.AttackAgent.BaseCommands import ParseRequest


def RunCommands():
    while CommandQueueNotEmpty():
        command = DeQueueCommand()
        request = ParseRequest(command)
        success = PerformRequest(request)
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


def CommandExists(userInput):
    return userInput in CommandsSwitch.keys()


def PerformRequest(request):
    if not request:
        return False
    command = str.lower(request[0])
    if command == "-help":
        HelpRequested()
        return True
    if not CommandExists(command):
        PrintAndLog(f"No such command '{command}'")
        return False
    try:
        PrintBlueAndLog(f"Running Command:    {' '.join(request)}")
        CommandsSwitch[command](request[1:])
        return True
    except Exception as ex:
        PrintAndLog(f"Failed to execute command {command}:\n")
        PrintRedAndLog(ex)
        return False

