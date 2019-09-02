#!/usr/bin/python3
import ntpath
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog
from os import listdir
from os.path import isfile, join


SupportedRequestTypes = ["-help", "-f", "-p"]
PreMadeBatchCommandsPath = "Agent\\BatchCommands\Scripts\\"


def GetAllPreMadeBatchNames():
    return [f for f in listdir(PreMadeBatchCommandsPath) if isfile(join(PreMadeBatchCommandsPath, f))]


def HelpRequested():
    text = "\n" \
           "        Run references text files containing a row delimited list of commands to run," \
           " places these commands at the front of the queue\n"\
           "        Command format:\n" \
           "                     run [-f] [filePath]\n" \
           "                     run [-p] [CommandsBatchName]\n\n" \
           "       Command parameters:\n" \
           "                     '-f' - Indicates you will pass a file path to the batch command file, this will be" \
           " followed by the filePath parameter\n" \
           "                     '-p' - Indicating you wish to use one of the pre made batch command scripts, will be " \
           "followed by the CommandsBatchName parameter\n" \
           "                     'filePath' - the full path to the batch command file - The batch file referenced " \
           "must contain only commands as provided when normally calling the attack agent\n" \
           "                     'CommandsBatchName' - The name of the pre made batch commands script\n\n" \
           "       The available scenarios are:\n"
    for commandName in GetAllPreMadeBatchNames():
        text = f"{text}" \
               f"                     {commandName}\n"
    text = f"{text}\n" \
           "        Each command must be separated by a new line\n" \
           "        It is possible to recursively add additional batch -run calls using a batch file\n" \
           "        Lines in Command Batch Files can be commented out by adding # to the start of the line\n"
    PrintAndLog(text)


def RunScenario(request, context):
    if not request:
        PrintRedAndLog("Missing required parameters")
        return

    requestType = request[0]

    if requestType not in SupportedRequestTypes:
        PrintRedAndLog(f"No such scenario command type: '{requestType}'")
        return

    if "-help" in request:
        HelpRequested()
        return

    if len(request) < 2:
        PrintRedAndLog("Missing parameters in request")
        return

    filePath = request[1]

    if requestType == "-p":
        if filePath not in GetAllPreMadeBatchNames():
            PrintRedAndLog(f"No such PreMade batch command: '{filePath}'")
            return
        filePath = f"{PreMadeBatchCommandsPath}{filePath}"
    try:
        with open(filePath, "r") as file:
            commandLines = list(filter(lambda a: not a.startswith('#'), list(file.read().splitlines())))
            PrintAndLog(f"Adding {len(commandLines)} Commands from {ntpath.basename(filePath)}")
            context.EnqueueCommandsNext(commandLines)
        file.close()
    except Exception as ex:
        print(f"Failed to load command batch file, exception encountered:\n")
        PrintRedAndLog(ex)


RunScenario.PublicFacing = "run"
