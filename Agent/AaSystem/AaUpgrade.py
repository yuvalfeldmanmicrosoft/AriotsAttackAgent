from Agent.AaSystem.SystemInspector import GetOperatingSystemName
from Agent.AttackAgent.Bash.BashCommandExecutor import RunSubProcess
from Agent.AaSystem.Log import PrintRedAndLog, PrintAndLog


def UpgradeAaToLatestVersion(request):
    try:
        if str.lower(GetOperatingSystemName()) != "linux":
            PrintRedAndLog("Failed to upgrade AttackAgent. Upgrade currently supported only in Linux")
            return
        RunSubProcess("cd /home/AriotsAttackAgent;sudo git checkout -f HEAD;sudo git pull;sudo chmod +x AttackAgent.py;")
    except Exception as ex:
        PrintAndLog(f"Failed to upgrade AttackAgent. Upgrade currently supported only in Linux. Ensure you have"
              f"required permissions and the Attack Agent is not running in another process.")
        PrintRedAndLog(ex)
