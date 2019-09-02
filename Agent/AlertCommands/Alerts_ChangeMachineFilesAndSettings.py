#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def RemovelOfSystemLogs(request, context):
    if "-help" in request:
        Help_RemovelOfSystemLogs()
        return

    context.EnqueueCommandsNext(["deletefiles -f /var/log/lastlog"])


def Ransomware(request, context):
    if "-help" in request:
        Help_Ransomware()
        return

    context.EnqueueCommandsNext(["createFile -f test.GNNCRY"])


def OverrideLinuxFiles(request, context):
    if "-help" in request:
        Help_OverrideLinuxFiles()
        return

    context.EnqueueCommandsNext(["copyfile -f /bin/netstat a"])


def LinuxBackdoor(request, context):
    if "-help" in request:
        Help_LinuxBackdoor()
        return

    context.EnqueueCommandsNext(["createfile -f-bus notifier"])


def FairwareMalware(request, context):
    if "-help" in request:
        Help_FairwareMalware()
        return

    context.EnqueueCommandsNext(["deletefiles /data/"])


def EgressData(request, context):
    if "-help" in request:
        Help_EgressData()
        return

    context.EnqueueCommandsNext(["servicestop bash /dev/tcp/"])


def DisableFirewall(request, context):
    if "-help" in request:
        Help_DisableFirewall()
        return

    context.EnqueueCommandsNext(["createfile -f f0VMRgIBAQ"])


def CommonBots(request, context):
    if "-help" in request:
        Help_CommonBots()
        return

    context.EnqueueCommandsNext(["createfile -f RTEGFN01.dat"])


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
