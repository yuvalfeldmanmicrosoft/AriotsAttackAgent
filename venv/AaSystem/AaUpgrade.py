from venv.AttackAgent.Bash.BashCommandExecutor import RunSubProcess
from venv.AaSystem.Colors import PrintRed
from venv.AaSystem.SystemInspector import GetOperatingSystemName


def UpgradeAaToLatestVersion(request):
    try:
        if str.lower(GetOperatingSystemName()) != "linux":
            PrintRed("Failed to upgrade AttackAgent. Upgrade currently supported only in Linux")
            return
        RunSubProcess("cd /home/AriotsAttackAgent;sudo git checkout -f HEAD;sudo git pull;sudo chmod +x AttackAgent.py;")
    except Exception as ex:
        print(f"Failed to upgrade AttackAgent. Upgrade currently supported only in Linux. Ensure you have"
              f"required permissions and the Attack Agent is not running in another process.")
        PrintRed(ex)

