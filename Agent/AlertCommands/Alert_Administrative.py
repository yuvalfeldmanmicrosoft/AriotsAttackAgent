#!/usr/bin/python3
from AaSystem.EventQueue.CommandQueue import EnqueueCommandsNext
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def AddSuspiciousUser(request):
    if "-help" in request:
        Help_AddSuspiciousUser()
        return
    EnqueueCommandsNext(["adduser -g 0"])


def PrivilegedContainer(request):
    if "-help" in request:
        Help_PrivilegedContainer()
        return

    return RunSubProcess("docker run redis --privileged")


def DisableAuditdLogging(request):
    if "-help" in request:
        Help_DisableAuditdLogging()
        return
    EnqueueCommandsNext(["servicestop auditd"])


def SuspiciousNohup(request):
    if "-help" in request:
        Help_SuspiciousNohup()
        return

    return RunSubProcess("nohup cat /tmp/")


def Help_AddSuspiciousUser():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo useradd aaa -g 0'\n"
                       "       Triggers alert: 'AddSuspiciousUser'\n")


def Help_SuspiciousNohup():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'nohup cat /tmp/'\n"
                       "       Triggers alert: 'SuspiciousNohup'\n")


def Help_PrivilegedContainer():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'docker run redis --privileged'\n"
                       "       Triggers alert: 'PrivilegedContainer'\n")


def Help_DisableAuditdLogging():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo service auditd stop'\n"
                       "       Triggers alert: 'DisableAuditdLogging'\n")


AddSuspiciousUser.PublicFacing = "addsuspicioususer"
SuspiciousNohup.PublicFacing = "suspiciousnohup"
PrivilegedContainer.PublicFacing = "privilegedcontainer"
DisableAuditdLogging.PublicFacing = "disableauditdlogg"