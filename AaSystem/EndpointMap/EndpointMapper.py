#!/usr/bin/python3
from AaSystem.EndpointMap.EndpointMap import CommandMappingNameByTree, CommandMapping
from AaSystem.Reflection.Reflect import GetPublicFacingFunctionsFromPath
import Agent.Commands.BashCommands.Bash_AdministrativeCommands
import Agent.Commands.BashCommands.Bash_ChangeMachineFilesAndSettings
import Agent.Commands.BashCommands.Bash_CustomCommand
import Agent.Commands.BashCommands.Bash_FileRetrieval
import Agent.Commands.BashCommands.Bash_InformationRetreivingCommands
import Agent.Commands.BashCommands.Bash_ProcessAndPortCommands
import Agent.Commands.AlertCommands.Alert_Administrative
import Agent.Commands.AlertCommands.Alerts_ChangeMachineFilesAndSettings
import Agent.Commands.AlertCommands.Alerts_FileRetrieval
import Agent.Commands.AlertCommands.Alerts_ProcessAndPorts
import Agent.Commands.SystemCommands.AaSystemCommands
import Agent.Commands.ProcessControl.ProcessCommands
import Agent.Commands.BatchCommands.BatchCommandHandler
import Agent.Commands.BasicHelpers.BasicHelpCommands
import AaSystem.AaSystemControl.AaUpgrade

CommandTypes = {
    "Bash":
        [
            "Agent.Commands.BashCommands.Bash_AdministrativeCommands",
            "Agent.Commands.BashCommands.Bash_ChangeMachineFilesAndSettings",
            "Agent.Commands.BashCommands.Bash_CustomCommand",
            "Agent.Commands.BashCommands.Bash_FileRetrieval",
            "Agent.Commands.BashCommands.Bash_InformationRetreivingCommands",
            "Agent.Commands.BashCommands.Bash_ProcessAndPortCommands",
        ],
    "Alerts":
        [
            "Agent.Commands.AlertCommands.Alert_Administrative",
            "Agent.Commands.AlertCommands.Alerts_ChangeMachineFilesAndSettings",
            "Agent.Commands.AlertCommands.Alerts_FileRetrieval",
            "Agent.Commands.AlertCommands.Alerts_ProcessAndPorts",
        ],
    "System":
        [
            "Agent.Commands.ProcessControl.ProcessCommands"
        ],
    "Scenario":
        [
            "Agent.Commands.BatchCommands.BatchCommandHandler"
        ],
    "BasicHelp":
        [
            "Agent.Commands.BasicHelpers.BasicHelpCommands"
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
