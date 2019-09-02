#!/usr/bin/python3
from AaSystem.EventQueue.CommandQueue import EnqueueCommandsNext
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def RemovelOfSystemLogs(request):
    if "-help" in request:
        Help_RemovelOfSystemLogs()
        return

    EnqueueCommandsNext(["deletefiles -f /var/log/lastlog"])


def Ransomware(request):
    if "-help" in request:
        Help_Ransomware()
        return

    EnqueueCommandsNext(["createFile -f test.GNNCRY"])


def OverrideLinuxFiles(request):
    if "-help" in request:
        Help_OverrideLinuxFiles()
        return

    EnqueueCommandsNext(["copyfile -f /bin/netstat a"])


def LinuxBackdoor(request):
    if "-help" in request:
        Help_LinuxBackdoor()
        return

    EnqueueCommandsNext(["createfile -f-bus notifier"])


def FairwareMalware(request):
    if "-help" in request:
        Help_FairwareMalware()
        return

    EnqueueCommandsNext(["deletefiles /data/"])


def EgressData(request):
    if "-help" in request:
        Help_EgressData()
        return

    return RunSubProcess("bash /dev/tcp/")


def DisableFirewall(request):
    if "-help" in request:
        Help_DisableFirewall()
        return

    EnqueueCommandsNext(["createfile -f f0VMRgIBAQ"])


def CommonBots(request):
    if "-help" in request:
        Help_CommonBots()
        return

    EnqueueCommandsNext(["createfile -f RTEGFN01.dat"])


def Help_RemovelOfSystemLogs():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm /var/log/lastlog'\n"
                       "       Triggers alert: 'RemovelOfSystemLogs'\n")


def Help_Ransomware():
    return PrintAndLog("\n"
                       "Performs the bash command: 'touch test.GNNCRY'\n"
                       "Triggers alert: 'Ransomware'\n")


def Help_OverrideLinuxFiles():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'cp /bin/netstat a'\n"
                       "       Triggers alert: 'OverrideLinuxFiles'\n")


def Help_LinuxBackdoor():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch d-bus notifier'\n"
                       "       Triggers alert: 'LinuxBackdoor'\n")


def Help_FairwareMalware():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'rm -rf /data/'\n"
                       "       Triggers alert: 'FairwareMalware'\n")


def Help_EgressData():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'bash /dev/tcp/'\n"
                       "       Triggers alert: 'EgressData'\n")


def Help_DisableFirewall():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch f0VMRgIBAQ'\n"
                       "       Triggers alert: 'DisableFirewall'\n")


def Help_CommonBots():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'touch RTEGFN01.dat'\n"
                       "       Triggers alert: 'CommonBots'\n")


RemovelOfSystemLogs.PublicFacing = "removelofsystemlogs"
Ransomware.PublicFacing = "ransomware"
OverrideLinuxFiles.PublicFacing = "overridelinuxfiles"
LinuxBackdoor.PublicFacing = "linuxbackdoor"
FairwareMalware.PublicFacing = "fairwaremalware"
EgressData.PublicFacing = "egressdata"
DisableFirewall.PublicFacing = "disablefirewall"
CommonBots.PublicFacing = "commonbots"
