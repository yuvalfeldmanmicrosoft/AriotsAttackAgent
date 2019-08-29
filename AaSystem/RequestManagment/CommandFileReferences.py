#!/usr/bin/python3
import Agent.ProcessControl.ProcessCommands
import Agent.BashCommands.BashCommands
import Agent.SystemCommands.AaSystemCommands
import Agent.BatchCommands.BatchCommandHandler
import AaSystem.AaSystemControl.AaUpgrade

CommandTypes = {
    "bc": ["Agent.BashCommands.BashCommands"],
    "sc": ["Agent.SystemCommands.AaSystemCommands",
           "Agent.ProcessControl.ProcessCommands"],
    "run": ["Agent.BatchCommands.BatchCommandHandler"],
    "BasicHelp": ["AaSystem.RequestManagment.RequestProcessor"],
    "System": ["AaSystem.AaSystemControl.AaUpgrade"],
}
