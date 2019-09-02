#!/usr/bin/python3
import os
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def GitClone(request, context):
    if "-help" in request:
        Help_GitClone()
        return

    if not request or len(request) < 1:
        PrintRedAndLog("Missing required parameters")

    clonePath = request[0]

    if len(request) == 2:
        return RunSubProcess(f"git clone {clonePath} {request[1]}")

    return RunSubProcess(f"git clone {clonePath}")


def DownloadFile(request, context):
    if "-help" in request:
        Help_DownloadFile()
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")

    destinationPath = request[0]
    filePath = request[1]

    return RunSubProcess(f"sudo wget -O {destinationPath} {filePath}")


def RetrieveFile(request, context):
    if "-help" in request:
        Help_RetrieveFile()
        return

    if not request or len(request) < 1:
        PrintRedAndLog("Missing required parameters")

    filePath = request[0]

    return RunSubProcess(f"curl {filePath}")


def Help_GitClone():
    return PrintAndLog("\n"
                       "       Clones a public git repository'\n"
                       "       gitclone [path] [cloneDestination=optional]\n"
                       "                'path' = the full clone url\n"
                       "                'cloneDestination' = an optional path indicating the destination to clone to\n"
                       )


def Help_DownloadFile():
    return PrintAndLog("\n"
                       "        downloadfile [destination] [fileURL]\n"
                       "                'destination' - the destination the file will be downloaded to"

                       "                'fileURL' - the URL to the file being downloaded")


def Help_RetrieveFile():
    return PrintAndLog("\n"
                       "        Performs the curl command to get a file into the terminal\n"
                       "        retrievefile [fileURL]\n"
                       "                'fileURL' - the URL to the file being downloaded\n")


GitClone.PublicFacing = "gitclone"
DownloadFile.PublicFacing = "downloadfile"
RetrieveFile.PublicFacing = "retrievefile"
