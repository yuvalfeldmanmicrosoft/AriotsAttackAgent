#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from Agent.BashCommands.BashCommandExecutor import RunSubProcess


def DeleteFiles(request):
    if "-help" in request:
        Help_DeleteFiles()
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")

    deleteType = request[0]
    path = request[1]

    if deleteType == "-f":
        return RunSubProcess(f"sudo rm {path}")
    if deleteType == "-d":
        return RunSubProcess(f"sudo rm -rf {path}")

    PrintRedAndLog("Invalid parameter passed")


def CreateFile(request):
    if "-help" in request:
        Help_DeleteFiles()
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")

    createType = request[0]
    path = request[1]

    if createType == "-f":
        return RunSubProcess(f"sudo touch {path}")
    if createType == "-f-bus":
        return RunSubProcess(f"sudo touch d-bus {path}")
    if createType == "-d":
        return RunSubProcess(f"sudo mkdir -p {path}")

    PrintRedAndLog("Invalid parameter passed")


def CopyFile(request):
    if "-help" in request:
        Help_DeleteFiles()
        return

    if not request or len(request) < 3:
        PrintRedAndLog("Missing required parameters")

    createType = request[0]
    originPath = request[1]
    destinationPath = request[2]

    if createType == "-f":
        return RunSubProcess(f"sudo cp {originPath} {destinationPath}")
    if createType == "-d":
        return RunSubProcess(f"sudo cp -avr {originPath} {destinationPath}")

    PrintRedAndLog("Invalid parameter passed")


def Help_DeleteFiles():
    return PrintAndLog("\n"
                       "       Deletes a file or directory'\n"
                       "       deletefiles [deleteType] [path]\n"
                       "                deleteType options:\n"
                       "                     '-f' - Delete single file\n"
                       "                     '-d' - Delete entire directory and all its contents\n"
                       "                'path' - the path of the file being creating including its name"
                       )


def Help_CreateFile():
    return PrintAndLog("\n"
                       "       Creates a file or directory'\n"
                       "       createfile [creationType] [path]\n"
                       "                creationType options:\n"
                       "                     '-f' - Create single empty file\n"
                       "                     '-f-bus' - Create single empty file on the d-bus\n"
                       "                     '-d' - Create a single empty directory\n"
                       )


def Help_CopyFile():
    return PrintAndLog("\n"
                       "       Copies a file or directory'\n"
                       "       copyfile [copyType] [originPath] [destinationPath]\n"
                       "                copyType options:\n"
                       "                     '-f' - Copy single empty file\n"
                       "                     '-d' - Copy a single empty directory\n"
                       "                'originPath' - the file or directory to copy\n"
                       "                'destinationPath' - the path where the copy will be created\n"
                       )


DeleteFiles.PublicFacing = "deletefiles"
CreateFile.PublicFacing = "createfile"
CopyFile.PublicFacing = "copyfile"
