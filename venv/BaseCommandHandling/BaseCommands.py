from venv.BaseCommandHandling.BatchCommandHandler import AddCommandsBatch
from venv.AttackAgent.Bash.BashCommands import RunBashCommand


def AddBatchCommands(request):
    AddCommandsBatch(request)


def BashAttackCommand(request):
    RunBashCommand(request)


CommandsSwitch = {
    "-ba": BashAttackCommand,
    "-run": AddCommandsBatch
}
