#!/usr/bin/python3
import time
from Agent.AaSystem.Log import PrintRedAndLog, PrintAndLog
from Agent.AttackAgent.BaseCommands import EnqueueCommandsNext

TimeConversionsFromSeconds = {
    "-s": 1,
    "-m": 60,
    "-h": 3600,
    "-d": 86400
}


class AaSystemCommands:
    def Wait(self, request):
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

    def Loop(self, request):
        if not request or len(request) < 2:
            PrintRedAndLog("Missing required parameters")
            return
        iterations = request[0]
        command = request[1]
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


class AaSystemCommandsHelp:
    def Wait(self, request):
        PrintAndLog("Sleeps for a requested amount of time\n"
                    "Command parameters: [WaitTimeType] [WaitTime]\n"
                    "'WaitTimeType' - The time format that for the WaitTime parameter, available options:\n"
                    "     -s: seconds\n"
                    "     -m: minutes\n"
                    "     -h: hours\n"
                    "     -d: days\n"
                    "'WaitTime: The amount of time that will be waited'")

    def Loop(self, request):
        PrintAndLog("A for loop on the provided function\n"
                    "Command parameteres: [Repetitions] [Command]\n"
                    "'Repetitions' - An integer indicating the amount of times to perform the provided function\n"
                    "'Command' - an Attack Agent function surrounded by parentheses that will be repeated in the loop")


def AaSystemCommandsSwitch(helpRequested=False):
    commands = AaSystemCommands() if not helpRequested else AaSystemCommandsHelp()
    switchOptions = {
        'wait': commands.Wait,
        'loop': commands.Loop
    }

    return switchOptions


def HelpRequested(availableCommands):
    text = "sc: Stands for System Commands. sc run system and program functions such as waiting, changing system "\
           "The available system commands are:\n"
    for command in availableCommands:
        text = f"{text}    {command}\n"
    text = f"{text}For more information on a command add -help after a command, i.e.: '-sc wait -help'"
    PrintAndLog(text)


def RunAaSystemCommand(request):
    if not request:
        PrintRedAndLog(f"No Attack Agent system command to execute passed in parameters")
        return
    command = str.lower(request[0])
    availableAaSystemCommands = AaSystemCommandsSwitch().keys()
    if command == "-help":
        HelpRequested(availableAaSystemCommands)
        return
    if command not in availableAaSystemCommands:
        PrintRedAndLog(f"No such Attack Agent system command: '{command}'")
        return
    AaSystemCommandHelpRequested = "-help" in request
    AaSystemCommandsSwitch(AaSystemCommandHelpRequested)[command](request[1:])
