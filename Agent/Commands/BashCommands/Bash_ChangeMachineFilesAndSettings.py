#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class DeleteFiles(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        deleteType = self.request[0]
        path = self.request[1]

        if deleteType == "-f":
            return RunSubProcess(f"sudo rm {path}")
        if deleteType == "-d":
            return RunSubProcess(f"sudo rm -rf {path}")

        PrintRedAndLog("Invalid parameter passed")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Deletes a file or directory'\n"
                           "       deletefiles [deleteType] [path]\n"
                           "                deleteType options:\n"
                           "                     '-f' - Delete single file\n"
                           "                     '-d' - Delete entire directory and all its contents\n"
                           "                'path' - the path of the file being creating including its name"
                           )


class CreateFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        createType = self.request[0]
        path = self.request[1]

        if createType == "-f":
            return RunSubProcess(f"sudo touch {path}")
        if createType == "-f-bus":
            return RunSubProcess(f"sudo touch d-bus {path}")
        if createType == "-d":
            return RunSubProcess(f"sudo mkdir -p {path}")

        PrintRedAndLog("Invalid parameter passed")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Creates a file or directory'\n"
                           "       createfile [creationType] [path]\n"
                           "                creationType options:\n"
                           "                     '-f' - Create single empty file\n"
                           "                     '-f-bus' - Create single empty file on the d-bus\n"
                           "                     '-d' - Create a single empty directory\n"
                           )


class CopyFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(3):
            return
        createType = self.request[0]
        originPath = self.request[1]
        destinationPath = self.request[2]

        if createType == "-f":
            return RunSubProcess(f"sudo cp {originPath} {destinationPath}")
        if createType == "-d":
            return RunSubProcess(f"sudo cp -avr {originPath} {destinationPath}")

        PrintRedAndLog("Invalid parameter passed")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Copies a file or directory'\n"
                           "       copyfile [copyType] [originPath] [destinationPath]\n"
                           "                copyType options:\n"
                           "                     '-f' - Copy single file\n"
                           "                     '-d' - Copy a single directory\n"
                           "                'originPath' - the file or directory to copy\n"
                           "                'destinationPath' - the path where the copy will be created\n"
                           )


DeleteFiles.PublicFacing = "deletefiles"
CreateFile.PublicFacing = "createfile"
CopyFile.PublicFacing = "copyfile"
