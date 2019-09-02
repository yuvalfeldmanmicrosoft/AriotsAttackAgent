#!/usr/bin/python3
import Agent.ProcessControl.ProcessCommands
import Agent.SystemCommands.AaSystemCommands
import Agent.BatchCommands.BatchCommandHandler
import AaSystem.AaSystemControl.AaUpgrade
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

CommandTypes = {
    "bc":
        [
            "Agent.BashCommands.Bash_AdministrativeCommands",
            "Agent.BashCommands.Bash_ChangeMachineFilesAndSettings",
            "Agent.BashCommands.Bash_CustomCommand",
            "Agent.BashCommands.Bash_FileRetrieval",
            "Agent.BashCommands.Bash_InformationRetreivingCommands",
            "Agent.BashCommands.Bash_ProcessAndPortCommands",
        ],
    "alerts":
        [
            "Agent.AlertCommands.Alert_Administrative",
            "Agent.AlertCommands.Alerts_ChangeMachineFilesAndSettings",
            "Agent.AlertCommands.Alerts_FileRetrieval",
            "Agent.AlertCommands.Alerts_ProcessAndPorts",
        ],
    "sc":
        [
            "Agent.SystemCommands.AaSystemCommands",
            "Agent.ProcessControl.ProcessCommands"
        ],
    "run":
        [
            "Agent.BatchCommands.BatchCommandHandler"
        ],
    "BasicHelp":
        [
            "AaSystem.RequestManagment.RequestProcessor"
        ],
    "System":
        [
            "AaSystem.AaSystemControl.AaUpgrade"
        ],
}
