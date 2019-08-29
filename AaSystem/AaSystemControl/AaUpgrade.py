#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintRedAndLog, PrintAndLog
from AaSystem.OperatingSystem.SystemInspector import GetOperatingSystemName
from Agent.AttackAgent.BashCommands.BashCommandExecutor import RunSubProcess


def UpgradeAaToLatestVersion(request):
    if "-help" in request:
        HelpRequested()
        return
    try:
        if str.lower(GetOperatingSystemName()) != "linux":
            PrintRedAndLog("Failed to upgrade AttackAgent. Upgrade currently supported only in Linux")
            return
        RunSubProcess("cd /home/AriotsAttackAgent;sudo git checkout -f HEAD;sudo git pull;sudo chmod +x AttackAgent.py;")
    except Exception as ex:
        PrintAndLog(f"Failed to upgrade AttackAgent. Upgrade currently supported only in Linux. Ensure you have"
              f"required permissions and the Attack Agent is not running in another process.")
        PrintRedAndLog(ex)


def HelpRequested():
    PrintAndLog("\n"
                "       Upgrade downloads and installs the latest stable version of Attack Agent, ensures Attack Agent"
                " Permissions are set and the $PATH variable is updated.\n"
                "       Currently Attack Agent Upgrade is only supported on Linux machines.")


UpgradeAaToLatestVersion.PublicFacing = "upgrade"
