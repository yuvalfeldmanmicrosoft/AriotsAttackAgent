#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def AddUser(request):
    if "-help" in request:
        Help_AddUser()
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
        return
    userType = request[0]
    if userType == "-r":
        return RunSubProcess(f"sudo useradd {request[0]}")
    if userType == "-a":
        return RunSubProcess(f"sudo useradd {request[0]} sudo")
    if userType == "-g":
        if len(request) < 2:
            PrintRedAndLog("Missing required parameters")
        return RunSubProcess(f"sudo useradd {request[0]} -g {request[1]}")
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


def Help_AddUser():
    return PrintAndLog("\n"
                       "       Adds a user to the operating system.\n"
                       "       useradd [Type] [Username]\n"
                       "                     'Type' - indicated the type of user that will be created, currently"
                       " supporting:\n"
                       "                             '-r' - regular user\n"
                       "                             '-a' - admin user\n"
                       "                             '-g' - add to group, must also pass a userID the user will "
                       "be associated with\n"
                       "                     'Username' - a string that is the username that will be created")


def Help_ChangeUserPassword():
    return PrintAndLog("\n"
                       "Changes the password for a user\n"
                       "       changeuserpassword [NewPassword] [User]\n"
                       "                     'NewPassword' - the new password that will be set for user\n"
                       "                     'User' - the username of the user\n")


AddUser.PublicFacing = "adduser"
ChangeUserPassword.PublicFacing = "changeuserpassword"
