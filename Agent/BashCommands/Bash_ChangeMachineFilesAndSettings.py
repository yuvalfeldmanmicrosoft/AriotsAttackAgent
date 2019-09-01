#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def RemovelOfSystemLogs(request):
    if "-help" in request:
        Help_RemovelOfSystemLogs()
        return

    return RunSubProcess("rm /var/log/lastlog")


def Ransomware(request):
    if "-help" in request:
        Help_Ransomware()
        return

    return RunSubProcess("touch test.GNNCRY")


def OverrideLinuxFiles(request):
    if "-help" in request:
        Help_OverrideLinuxFiles()
        return

    return RunSubProcess("cp /bin/netstat a")


def LinuxBackdoor(request):
    if "-help" in request:
        Help_LinuxBackdoor()
        return

    return RunSubProcess("touch d-bus notifier")


def FairwareMalware(request):
    if "-help" in request:
        Help_FairwareMalware()
        return

    return RunSubProcess("rm -rf /data/")


def EgressData(request):
    if "-help" in request:
        Help_EgressData()
        return

    return RunSubProcess("bash /dev/tcp/")


def DisableFirewall(request):
    if "-help" in request:
        Help_DisableFirewall()
        return

    return RunSubProcess("touch f0VMRgIBAQ")


def CommonBots(request):
    if "-help" in request:
        Help_CommonBots()
        return

    return RunSubProcess("touch RTEGFN01.dat")


def ClearHistoryFile(request):
    if "-help" in request:
        Help_ClearHistoryFile()
        return

    return RunSubProcess("history -c")


def Help_RemovelOfSystemLogs():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm /var/log/lastlog'\n"
                       "       Triggers alert: 'RemovelOfSystemLogs'")


def Help_Ransomware():
    return PrintAndLog("\n"
                       "Performs the bash command: 'touch test.GNNCRY'\n"
                       "Triggers alert: 'Ransomware'")


def Help_OverrideLinuxFiles():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'cp /bin/netstat a'\n"
                       "       Triggers alert: 'OverrideLinuxFiles'")


def Help_LinuxBackdoor():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch d-bus notifier'\n"
                       "       Triggers alert: 'LinuxBackdoor'")


def Help_FairwareMalware():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm -rf /data/'\n"
                       "       Triggers alert: 'FairwareMalware'")


def Help_EgressData():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'bash /dev/tcp/'\n"
                       "       Triggers alert: 'EgressData'")


def Help_DisableFirewall():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch f0VMRgIBAQ'\n"
                       "       Triggers alert: 'DisableFirewall'")


def Help_CommonBots():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch RTEGFN01.dat'\n"
                       "       Triggers alert: 'CommonBots'")


def Help_ClearHistoryFile():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'history -c'\n"
                       "       Triggers alert: 'ClearHistoryFile'")


RemovelOfSystemLogs.PublicFacing = "removelofsystemlogs"
Ransomware.PublicFacing = "ransomware"
OverrideLinuxFiles.PublicFacing = "overridelinuxfiles"
LinuxBackdoor.PublicFacing = "linuxbackdoor"
FairwareMalware.PublicFacing = "fairwaremalware"
EgressData.PublicFacing = "egressdata"
DisableFirewall.PublicFacing = "disablefirewall"
CommonBots.PublicFacing = "commonbots"
ClearHistoryFile.PublicFacing = "clearhistoryfile"
