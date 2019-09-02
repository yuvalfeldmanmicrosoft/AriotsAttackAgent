#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from AaSystem.EndpointMap.EndpointMap import CommandMappingNameByTree
from Agent.CommandInterface.ICommand import ICommand


def printHelpInfo(freeText, commandTree):
    text = f"{freeText}\n" \
           "       The available commands under this category are:\n\n"
    for command in CommandMappingNameByTree[commandTree]:
        text = f"{text}" \
               f"               {command}\n"
    text = f"{text}\n" \
           f"       Type -help with a command type of the listed commands to get additional information on that command"
    PrintAndLog(text)


class BaseCommandsHelp(ICommand):
    def Execute(self):
        self.HelpRequested()

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       All commands follow the format - [CommandName] [CommandsParameter] [CommandsParameter] "
                    "...\n"
                    "       Type -help with any CommandType for more information on that command\n\n"
                    "       Available commands types:\n"
                    "               Alerts               Performs Scenarios specifically targeted at raising IoT"
                    " alerts\n"
                    "               Bash                Uses bash commands to perform tasks\n"
                    "               Scenarios           References text files containing a row delimited list of "
                    "commands to run, places these commands at the front of the queue\n"
                    "               System              Perform program and environment commands such as waiting, "
                    "looping, handling environment variables and so on\n"
                    "               Upgrade             Upgrades to latest version of Ariots Attack Agent - "
                    "currently only supported on linux machines\n\n"
                    "       Type -help with a command type of the listed commands to get a list of available "
                    "commands for that command type")


class BashCommandList(ICommand):
    def Execute(self):
        if "-help" not in self.request:
            return
        self.HelpRequested()

    def HelpRequested(self):
        freeText = "       Uses bash commands to perform tasks"
        printHelpInfo(freeText, "Bash")


class AlertsCommandList(ICommand):
    def Execute(self):
        if "-help" not in self.request:
            return
        self.HelpRequested()

    def HelpRequested(self):
        freeText = "       Uses alerts commands to perform tasks"
        printHelpInfo(freeText, "Alerts")


class ScenariosCommandList(ICommand):
    def Execute(self):
        if "-help" not in self.request:
            return
        self.HelpRequested()

    def HelpRequested(self):
        freeText = "       References text files containing a row delimited list of commands " \
                   "to run, places these commands at the front of the queue"
        printHelpInfo(freeText, "Scenario")


class SystemCommandList(ICommand):
    def Execute(self):
        if "-help" not in self.request:
            return
        self.HelpRequested()

    def HelpRequested(self):
        freeText = "       Perform program and environment commands such as waiting, " \
                   "looping, handling environment variables and so on"
        printHelpInfo(freeText, "System")


BashCommandList.PublicFacing = "bash"
ScenariosCommandList.PublicFacing = "scenarios"
SystemCommandList.PublicFacing = "system"
AlertsCommandList.PublicFacing = "alerts"
BaseCommandsHelp.PublicFacing = "-help"
