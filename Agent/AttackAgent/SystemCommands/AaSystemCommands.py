#!/usr/bin/python3
import time
from AaSystem.LogAndPrint.Log import PrintRedAndLog, PrintAndLog
from AaSystem.EventQueue.CommandQueue import EnqueueCommandsNext

TimeConversionsFromSeconds = {
    "-s": 1,
    "-m": 60,
    "-h": 3600,
    "-d": 86400
}


def Wait(request):
    if "-help" in request:
        Help_Wait(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog(f"Missing system command parameters")
        return

    requestedTimeType = request[0]
    waitTimeRequested = request[1]

    if requestedTimeType not in TimeConversionsFromSeconds.keys():
        PrintRedAndLog(f"Requested wait type '{requestedTimeType}' not valid type")
        return

    try:
        WaitTime = float(waitTimeRequested) * TimeConversionsFromSeconds[requestedTimeType]
    except ValueError:
        PrintRedAndLog("The Wait time entered is not a valid number")
        return

    time.sleep(WaitTime)


def Loop(request):
    if request and request[0] == "-help":
        Help_Loop(request)
        return

    if not request or len(request) < 2:
        PrintRedAndLog("Missing required parameters")
        return
    iterations = request[0]
    command = ' '.join(request[1:])
    try:
        commandsList = []
        intIterations = int(iterations)
        for i in range(intIterations):
            commandsList.append(command)
        EnqueueCommandsNext(commandsList)
    except Exception as ex:
        PrintAndLog(f"Failed to execute Loop on repetitions: {iterations}, command: {command}:\n")
        PrintRedAndLog(ex)
        return


def Help_Wait(request):
    PrintAndLog("\n"
                "       Sleeps for a requested amount of time\n"
                "       Command parameters: [WaitTimeType] [WaitTime]\n"
                "                     'WaitTimeType' - The time format that for the WaitTime parameter,"
                " available options:\n"
                "                                   -s: seconds\n"
                "                                   -m: minutes\n"
                "                                   -h: hours\n"
                "                                   -d: days\n"
                "       'WaitTime: The amount of time that will be waited'\n")


def Help_Loop(request):
    PrintAndLog("\n"
                "       A for loop on the provided function\n"
                "       Command parameters: [Repetitions] [function]\n"
                "                     'Repetitions' - An integer indicating the amount of "
                "times to perform the provided function\n"
                "                     'function' - an Attack Agent function surrounded "
                "by parentheses that will be repeated in the loop\n")


Wait.PublicFacing = "wait"
Loop.PublicFacing = "loop"