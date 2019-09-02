#!/usr/bin/python3
import Agent.ProcessControl.ProcessCommands
import Agent.SystemCommands.AaSystemCommands
import Agent.BatchCommands.BatchCommandHandler
import Agent.BashCommands.Bash_AdministrativeCommands
import Agent.BashCommands.Bash_ChangeMachineFilesAndSettings
import Agent.BashCommands.Bash_CustomCommand
import Agent.BashCommands.Bash_FileRetrieval
import Agent.BashCommands.Bash_InformationRetreivingCommands
import Agent.BashCommands.Bash_ProcessAndPortCommands
import Agent.AlertCommands.Alert_Administrative
import Agent.AlertCommands.Alerts_ChangeMachineFilesAndSettings
import Agent.AlertCommands.Alerts_FileRetrieval
import Agent.AlertCommands.Alerts_ProcessAndPorts
import Agent.AlertCommands.Alerts_ProcessAndPorts
import Agent.BasicHelpers.BasicHelpCommands
import AaSystem.AaSystemControl.AaUpgrade
from AaSystem.RequestManagment.PublicEndpointMap import CommandMappingNameByTree, CommandMapping
from AaSystem.Reflection.Reflect import GetPublicFacingFunctionsFromPath

CommandTypes = {
    "Bash":
        [
            "Agent.BashCommands.Bash_AdministrativeCommands",
            "Agent.BashCommands.Bash_ChangeMachineFilesAndSettings",
            "Agent.BashCommands.Bash_CustomCommand",
            "Agent.BashCommands.Bash_FileRetrieval",
            "Agent.BashCommands.Bash_InformationRetreivingCommands",
            "Agent.BashCommands.Bash_ProcessAndPortCommands",
        ],
    "Alerts":
        [
            "Agent.AlertCommands.Alert_Administrative",
            "Agent.AlertCommands.Alerts_ChangeMachineFilesAndSettings",
            "Agent.AlertCommands.Alerts_FileRetrieval",
            "Agent.AlertCommands.Alerts_ProcessAndPorts",
        ],
    "System":
        [
            "Agent.SystemCommands.AaSystemCommands",
            "Agent.ProcessControl.ProcessCommands"
        ],
    "Scenario":
        [
            "Agent.BatchCommands.BatchCommandHandler"
        ],
    "BasicHelp":
        [
            "Agent.BasicHelpers.BasicHelpCommands"
        ],
    "Program":
        [
            "AaSystem.AaSystemControl.AaUpgrade"
        ],
}


def CreatePublicEndpointMap():
    for commandType in CommandTypes:
        if commandType not in CommandMappingNameByTree:
            CommandMappingNameByTree[commandType] = []
        for commandPath in CommandTypes[commandType]:
            commands = GetPublicFacingFunctionsFromPath(commandPath)
            for command in commands:
                CommandMapping[str.lower(command[1].PublicFacing)] = command[1]
                CommandMappingNameByTree[commandType].append(command[1].PublicFacing)
