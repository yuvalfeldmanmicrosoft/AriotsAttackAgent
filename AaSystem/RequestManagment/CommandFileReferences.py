#!/usr/bin/python3
import AaSystem.EventQueue.ProcessControl.ProcessCommands
import Agent.AttackAgent.BashCommands.BashCommands
import Agent.AttackAgent.SystemCommands.AaSystemCommands
import Agent.AttackAgent.BatchCommands.BatchCommandHandler
import AaSystem.AaSystemControl.AaUpgrade

CommandTypes = {
    "bc": ["Agent.AttackAgent.BashCommands.BashCommands"],
    "sc": ["Agent.AttackAgent.SystemCommands.AaSystemCommands",
           "AaSystem.EventQueue.ProcessControl.ProcessCommands"],
    "run": ["Agent.AttackAgent.BatchCommands.BatchCommandHandler"],
    "BasicHelp": ["AaSystem.RequestManagment.RequestProcessor"],
    "System": ["AaSystem.AaSystemControl.AaUpgrade"],
}
