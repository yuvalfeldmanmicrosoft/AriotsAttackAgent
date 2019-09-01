#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def AddSuspiciousUser(request):
    if "-help" in request:
        Help_AddSuspiciousUser()
        return

    return RunSubProcess("sudo useradd aaa -g 0")


def PrivilegedContainer(request):
    if "-help" in request:
        Help_PrivilegedContainer()
        return

    return RunSubProcess("docker run redis --privileged")


def DisableAuditdLogging(request):
    if "-help" in request:
        Help_DisableAuditdLogging()
        return

    return RunSubProcess("sudo service auditd stop")


def SuspiciousNohup(request):
    if "-help" in request:
        Help_SuspiciousNohup()
        return

    return RunSubProcess("nohup cat /tmp/")


def AddUser(request):
    if "-help" in request:
        Help_AddUser()
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
        Help_ChangeUserPassword()
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
    newPassword = request[0]
    user = request[1]
    return RunSubProcess(f"sudo {newPassword} {user}")


def Help_AddSuspiciousUser():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo useradd aaa -g 0'\n"
                       "       Triggers alert: 'AddSuspiciousUser'")


def Help_SuspiciousNohup():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'nohup cat /tmp/'\n"
                       "       Triggers alert: 'SuspiciousNohup'")


def Help_PrivilegedContainer():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'docker run redis --privileged'\n"
                       "       Triggers alert: 'PrivilegedContainer'")


def Help_DisableAuditdLogging():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'sudo service auditd stop'\n"
                       "       Triggers alert: 'DisableAuditdLogging'")


def Help_AddUser():
    return PrintAndLog("\n"
                       "       dds a user to the operating system.\n"
                       "       useradd [Type] [Username]\n"
                       "                     'Type' - indicated the type of user that will be created, currently"
                       " supporting:\n"
                       "                     '-r' - regular user\n"
                       "                     '-a' - admin user\n"
                       "                     'Username' - a string that is the username that will be created")


def Help_ChangeUserPassword():
    return PrintAndLog("\n"
                       "Changes the password for a user\n"
                       "       changeuserpassword [NewPassword] [User]\n"
                       "                     'NewPassword' - the new password that will be set for user\n"
                       "                     'User' - the username of the user")


AddSuspiciousUser.PublicFacing = "addsuspicioususer"
SuspiciousNohup.PublicFacing = "suspiciousnohup"
PrivilegedContainer.PublicFacing = "privilegedcontainer"
DisableAuditdLogging.PublicFacing = "disableauditdlogg"
AddUser.PublicFacing = "adduser"
ChangeUserPassword.PublicFacing = "changeuserpassword"
