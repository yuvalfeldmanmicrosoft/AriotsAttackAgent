#!/usr/bin/python3
import time
from AaSystem.LogAndPrint.Log import PrintRedAndLog, PrintAndLog
from Agent.CommandInterface.ICommand import ICommand
from Agent.Commands.ProcessControl.ProcessCommands import RunProcessPool

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
            self.context.CommandQueue.EnqueueCommandsNext(commandsList)
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


def ReplaceForEach(command, oldString, newStrings):
    return [command.replace(oldString, newString) for newString in newStrings]


def GetParamArrayFromFile(path):
    try:
        with open(path, "r") as file:
            parameters = list(file.read().splitlines())
            PrintAndLog(f"Adding {len(parameters)} commands using commands from {path}")
        file.close()
        splitParameters = []
        for param in parameters:
            if "," in param:
                splitParameters.extend(param.split(","))
                continue
            splitParameters.append(param)
        return splitParameters
    except Exception as ex:
        print(f"Failed to load command batch file, exception encountered:\n")
        PrintRedAndLog(ex)


def GetParamArrayFromString(string):
    if not string:
        return ""
    return string.split(",")


def GetCommandsFromSwapDictionary(command, swapDictionary):
    return []


def GetNewCommands(readSource, command, swaps):
    swapDictionary = {}

    for pair in swaps:
        kvp = str(pair).split("=")
        if len(kvp) != 2:
            PrintRedAndLog("Invalid syntax")
        if readSource == "-p":
            swapDictionary[kvp[0]] = GetParamArrayFromString(kvp[1])
        elif readSource == "-f":
            swapDictionary[kvp[0]] = GetParamArrayFromFile(kvp[1])
        else:
            PrintRedAndLog(f"No supported read source parameter {readSource}")
            return

    return GetCommandsFromSwapDictionary(command, swapDictionary)


class ForEach(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(3):
            return
        newCommands = GetNewCommands(self.request[0], self.request[1], self.request[2:])
        self.context.CommandQueue.EnqueueCommandsNext(newCommands)

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       A for loop on the provided function\n"
                    "       Command parameters: [Repetitions] [function]\n"
                    "                     'Repetitions' - An integer indicating the amount of "
                    "times to perform the provided function\n"
                    "                     'function' - an Attack Agent function surrounded "
                    "by parentheses that will be repeated in the loop\n")


class AsyncForEach(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(4):
            return
        newCommandsString = ' '.join(GetNewCommands(self.request[1], self.request[2], self.request[3:]))
        processPoolCommand = f"asyncpool {self.request[0]} {newCommandsString}"
        self.context.CommandQueue.EnqueueCommandsNext(processPoolCommand)

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
AsyncForEach.PublicFacing = "asyncforeach"
