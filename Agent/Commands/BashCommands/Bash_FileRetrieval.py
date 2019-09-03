#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.BashCommands.BashCommandExecutor import RunSubProcess


class GitClone(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        clonePath = self.request[0]
        if len(self.request) == 2:
            return RunSubProcess(f"git clone {clonePath} {self.request[1]}")
        return RunSubProcess(f"git clone {clonePath}")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Clones a public git repository'\n"
                           "       gitclone [path] [cloneDestination=optional]\n"
                           "                'path' = the full clone url\n"
                           "                'cloneDestination' = an optional path indicating the destination to clone to\n"
                           )


class DownloadFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        destinationPath = self.request[0]
        filePath = self.request[1]

        return RunSubProcess(f"sudo wget -O {destinationPath} {filePath}")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "        downloadfile [destination] [fileURL]\n"
                           "                'destination' - the destination the file will be downloaded to"
    
                           "                'fileURL' - the URL to the file being downloaded")


class RetrieveFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(1):
            return
        filePath = self.request[0]

        return RunSubProcess(f"curl {filePath}")

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "        Performs the curl command to get a file into the terminal\n"
                           "        retrievefile [fileURL]\n"
                           "                'fileURL' - the URL to the file being downloaded\n")


GitClone.PublicFacing = "gitclone"
DownloadFile.PublicFacing = "downloadfile"
RetrieveFile.PublicFacing = "retrievefile"
