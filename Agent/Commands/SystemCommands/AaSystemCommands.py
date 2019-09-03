#!/usr/bin/python3
import itertools
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
    valuesList = list(swapDictionary.values())
    keysList = list(swapDictionary.keys())
    allOptions = itertools.product(*valuesList)
    paramCount = len(keysList)
    results = []
    for option in allOptions:
        newCommand = command
        for i in range(paramCount):
            newCommand = newCommand.replace(keysList[i], option[i])
        results.append(newCommand)
    return results


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
                    "       foreach receives a command with keys that need to be replaced and a list of key value "
                    "pairs and creates commands of all the possible replacements for keys in the original command "
                    "with key value options\n"
                    "       Command parameters: [command] [keyValuePairType] [keyValuePairs] [keyValuePairs]...\n"
                    "                     'command' - The command that will be run. The command must be encased in"
                    "quotations and must have keys that will be replaced matching the key in the key value pairs\n"
                    "                     'keyValuePairType' - Can be either -p or -f:"
                    "                               '-p' - indicating the key value pair will be a key, an equals "
                    "sign and a list divided by commas\n"
                    "                               '-f' - indicating the key value pair will be a key, an quals"
                    "sign and a url to a list of values divided by commas\n"
                    "                       'keyValuePair' - a key which will be replaced in the command and a list"
                    "of values seperated by commas, a command option will be generated for each permutation available "
                    "of key value pairs\n\n"
                    "       for example: foreach -p 'custombash echo x' x='1,2,3' will result in three commands "
                    "replacing x with 1, 2 and 3\n"
                    "       additional example: foreach -p 'custombash echo x y' x='1,2,3' y='4,5,6 will result in 9"
                    "commands that will be executed for all the replacements of x and y with 1, 2, 3 and 4, 5, 6"
                    "respectively")


class AsyncForEach(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(4):
            return
        newCommands = GetNewCommands(self.request[1], self.request[2], self.request[3:])
        newCommandsString = ' '.join([f"\'{option}\'" for option in newCommands])
        processPoolCommand = f"asyncpool {self.request[0]} {newCommandsString}"
        self.context.CommandQueue.EnqueueCommandsNext([processPoolCommand])

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       asyncforeach works like foreach but receives an additional parameter processCount "
                    "indicating the amount of processes the workload will be split"
                    "       asyncforeach receives a command with keys that need to be replaced and a list of key value "
                    "pairs and creates commands of all the possible replacements for keys in the original command "
                    "with key value options\n"
                    "       Command parameters: [command] [processCount] [keyValuePairType] [keyValuePairs]"
                    " [keyValuePairs]...\n"
                    "                     'command' - The command that will be run. The command must be encased in"
                    "quotations and must have keys that will be replaced matching the key in the key value pairs\n"
                    "                     'processCount' - the amount of processes the commands created will run on"
                    "                     'keyValuePairType' - Can be either -p or -f:"
                    "                               '-p' - indicating the key value pair will be a key, an equals "
                    "sign and a list divided by commas\n"
                    "                               '-f' - indicating the key value pair will be a key, an quals"
                    "sign and a url to a list of values divided by commas\n"
                    "                       'keyValuePair' - a key which will be replaced in the command and a list"
                    "of values seperated by commas, a command option will be generated for each permutation available "
                    "of key value pairs\n\n"
                    "       for example: foreach -p 'custombash echo x' x='1,2,3' will result in three commands "
                    "replacing x with 1, 2 and 3\n"
                    "       additional example: foreach -p 'custombash echo x y' x='1,2,3' y='4,5,6 will result in 9"
                    "commands that will be executed for all the replacements of x and y with 1, 2, 3 and 4, 5, 6"
                    "respectively")


Wait.PublicFacing = "wait"
Loop.PublicFacing = "loop"
ForEach.PublicFacing = "foreach"
AsyncForEach.PublicFacing = "asyncforeach"
