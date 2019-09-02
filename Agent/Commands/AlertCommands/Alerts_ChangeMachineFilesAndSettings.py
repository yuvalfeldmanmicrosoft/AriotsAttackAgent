#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class RemovelOfSystemLogs(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["deletefiles -f /var/log/lastlog"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'rm /var/log/lastlog'\n"
                           "       Triggers alert: 'RemovelOfSystemLogs'\n")


class Ransomware(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["createFile -f test.GNNCRY"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "Performs the bash command: 'touch test.GNNCRY'\n"
                           "Triggers alert: 'Ransomware'\n")


class OverrideLinuxFiles(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["copyfile -f /bin/netstat a"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'cp /bin/netstat a'\n"
                           "       Triggers alert: 'OverrideLinuxFiles'\n")


class LinuxBackdoor(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["createfile -f-bus notifier"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'touch d-bus notifier'\n"
                           "       Triggers alert: 'LinuxBackdoor'\n")


class FairwareMalware(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["deletefiles /data/"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'rm -rf /data/'\n"
                           "       Triggers alert: 'FairwareMalware'\n")


class EgressData(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["servicestop bash /dev/tcp/"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'bash /dev/tcp/'\n"
                           "       Triggers alert: 'EgressData'\n")


class DisableFirewall(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["createfile -f f0VMRgIBAQ"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'touch f0VMRgIBAQ'\n"
                           "       Triggers alert: 'DisableFirewall'\n")


class CommonBots(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["createfile -f RTEGFN01.dat"])

    def HelpRequested(self):
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
