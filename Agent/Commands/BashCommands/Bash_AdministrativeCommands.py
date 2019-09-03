#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class AddUser(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        userType = self.request[0]
        if userType == "-r":
            return RunSubProcess(f"sudo useradd {self.request[0]}")
        if userType == "-a":
            return RunSubProcess(f"sudo useradd {self.request[0]} sudo")
        if userType == "-g":
            if len(self.request) < 2:
                PrintRedAndLog("Missing required parameters")
            return RunSubProcess(f"sudo useradd {self.request[0]} -g {self.request[1]}")
        PrintRedAndLog("Invalid parameter passed")
        return

    def HelpRequested(self):
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


class ChangeUserPassword(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        newPassword = self.request[0]
        user = self.request[1]
        return RunSubProcess(f"sudo {newPassword} {user}")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "Changes the password for a user\n"
                           "       changeuserpassword [NewPassword] [User]\n"
                           "                     'NewPassword' - the new password that will be set for user\n"
                           "                     'User' - the username of the user\n")


AddUser.PublicFacing = "adduser"
ChangeUserPassword.PublicFacing = "changeuserpassword"
