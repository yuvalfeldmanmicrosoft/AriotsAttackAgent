#!/usr/bin/python3
from Agent.AaSystem.AaUpgrade import UpgradeAaToLatestVersion
from Agent.AttackAgent.AttackAgentSystemCommands.AaSystemCommands import RunAaSystemCommand
from Agent.AttackAgent.BatchCommands.BatchCommandHandler import AddCommandsBatch
from Agent.AttackAgent.Bash.BashCommands import RunBashCommand


def AddBatchCommands(request):
    AddCommandsBatch(request)


def BashAttackCommand(request):
    RunBashCommand(request)


def AaSystemCommand(request):
    RunAaSystemCommand(request)


def AaUpgrade(request):
    UpgradeAaToLatestVersion(request)


CommandsSwitch = {
    "ba": BashAttackCommand,
    "run": AddCommandsBatch,
    "sc": AaSystemCommand,
    "upgrade": AaUpgrade
}
