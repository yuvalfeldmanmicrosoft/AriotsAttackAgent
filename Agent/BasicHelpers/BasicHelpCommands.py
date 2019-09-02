#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from AaSystem.EndpointMap.EndpointMap import CommandMappingNameByTree


def BaseCommandsHelp():
    PrintAndLog("\n"
                "       All commands follow the format - [CommandName] [CommandsParameter] [CommandsParameter] ...\n"
                "       Type -help with any CommandType for more information on that command\n\n"
                "       Available commands types:\n"
                "               Alerts               Performs Scenarios specifically targeted at raising IoT alerts\n"
                "               Bash                Uses bash commands to perform tasks\n"
                "               Scenarios           References text files containing a row delimited list of commands "
                "to run, places these commands at the front of the queue\n"
                "               System              Perform program and environment commands such as waiting, "
                "looping, handling environment variables and so on\n"
                "               Upgrade             Upgrades to latest version of Ariots Attack Agent - currently only "
                "supported on linux machines\n\n"
                "       Type -help with a command type of the listed commands to get a list of available commands for"
                "that command type")


def BashCommandList(request, context):
    if "-help" not in request:
        return
    freeText = "       Uses bash commands to perform tasks"
    printHelpInfo(freeText, "Bash")


def AlertsCommandList(request, context):
    if "-help" not in request:
        return
    freeText = "       Uses alerts commands to perform tasks"
    printHelpInfo(freeText, "Alerts")


def ScenariosCommandList(request, context):
    if "-help" not in request:
        return
    freeText = "       References text files containing a row delimited list of commands " \
               "to run, places these commands at the front of the queue"
    printHelpInfo(freeText, "Scenario")


def SystemCommandList(request, context):
    if "-help" not in request:
        return
    freeText = "       Perform program and environment commands such as waiting, " \
               "looping, handling environment variables and so on"
    printHelpInfo(freeText, "System")


def printHelpInfo(freeText, commandTree):
    text = f"{freeText}\n" \
           "       The available commands under this category are:\n\n"
    for command in CommandMappingNameByTree[commandTree]:
        text = f"{text}" \
               f"               {command}\n"
    text = f"{text}\n" \
           f"       Type -help with a command type of the listed commands to get additional information on that command"
    PrintAndLog(text)


BashCommandList.PublicFacing = "bash"
ScenariosCommandList.PublicFacing = "scenarios"
SystemCommandList.PublicFacing = "system"
AlertsCommandList.PublicFacing = "alerts"
