#!/usr/bin/python3
import time
from AaSystem.LogAndPrint.Log import PrintRedAndLog, PrintAndLog
from Agent.CommandInterface.ICommand import ICommand

TimeConversionsFromSeconds = {
    "-s": 1,
    "-m": 60,
    "-h": 3600,
    "-d": 86400
}


class Wait(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        requestedTimeType = self.request[0]
        waitTimeRequested = self.request[1]

        if requestedTimeType not in TimeConversionsFromSeconds.keys():
            PrintRedAndLog(f"Requested wait type '{requestedTimeType}' not valid type")
            return

        try:
            WaitTime = float(waitTimeRequested) * TimeConversionsFromSeconds[requestedTimeType]
        except ValueError:
            PrintRedAndLog("The Wait time entered is not a valid number")
            return

        time.sleep(WaitTime)

    def HelpRequested(self):
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

class Loop(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(2):
            return
        iterations = self.request[0]
        command = ' '.join(self.request[1:])
        try:
            commandsList = []
            intIterations = int(iterations)
            for i in range(intIterations):
                commandsList.append(command)
            self.context.EnqueueCommandsNext(commandsList)
        except Exception as ex:
            PrintAndLog(f"Failed to execute Loop on repetitions: {iterations}, command: {command}:\n")
            PrintRedAndLog(ex)
            return

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       A for loop on the provided function\n"
                    "       Command parameters: [Repetitions] [function]\n"
                    "                     'Repetitions' - An integer indicating the amount of "
                    "times to perform the provided function\n"
                    "                     'function' - an Attack Agent function surrounded "
                    "by parentheses that will be repeated in the loop\n")


Wait.PublicFacing = "wait"
Loop.PublicFacing = "loop"
