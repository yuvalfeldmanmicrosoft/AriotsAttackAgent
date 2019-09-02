#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class AddSuspiciousUser(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["adduser -g 0"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'sudo useradd aaa -g 0'\n"
                           "       Triggers alert: 'AddSuspiciousUser'\n")


class PrivilegedContainer(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext("custombash docker run redis --privileged")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'docker run redis --privileged'\n"
                           "       Triggers alert: 'PrivilegedContainer'\n")


class DisableAuditdLogging(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["servicestop auditd"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'sudo service auditd stop'\n"
                           "       Triggers alert: 'DisableAuditdLogging'\n")


class SuspiciousNohup(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["custombash nohup cat /tmp/"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'nohup cat /tmp/'\n"
                           "       Triggers alert: 'SuspiciousNohup'\n")


AddSuspiciousUser.PublicFacing = "addsuspicioususer"
SuspiciousNohup.PublicFacing = "suspiciousnohup"
PrivilegedContainer.PublicFacing = "privilegedcontainer"
DisableAuditdLogging.PublicFacing = "disableauditdlogg"
