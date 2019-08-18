#!/usr/bin/python3
import datetime
import os
from Agent.AaSystem.Colors import *
from Agent.AaSystem.SystemInspector import GetOperatingSystemName


def GetLogFileName():
    now = datetime.datetime.now()
    return f"AttackAgentLog{now.day}{now.month}{now.year}"


def GetLogsFolderPath():
    if str.lower(GetOperatingSystemName()) == "linux":
        return "~\\AriotsAttackAgent\\Logs"
    return "\\Logs"


def GetLogFilePath():
    return f".{GetLogsFolderPath()}\\{GetLogFileName()}.txt"


def CreateLogFolderIfNone():
    logsFolderPath = GetLogsFolderPath()
    if not os.path.exists(logsFolderPath):
        os.makedirs(logsFolderPath)


def WriteToLog(text):
    CreateLogFolderIfNone()
    f = open(GetLogFilePath(), "a+")
    f.write(f"{datetime.datetime.now()}: ")
    f.write(f"{text}\n")
    f.close()


def PrintColor(text, color):
    print(f"{color}{text}{CommandLineColors.ENDCOLOR}")


def PrintColorAndLog(text, color):
    print(f"{color}{text}{CommandLineColors.ENDCOLOR}")
    WriteToLog(text)


def PrintAndLog(text):
    print(text)
    WriteToLog(text)


def PrintHeader(text):
    PrintColor(text, CommandLineColors.HEADER)


def PrintBlue(text):
    PrintColor(text, CommandLineColors.OKBLUE)


def PrintGreen(text):
    PrintColor(text, CommandLineColors.OKGREEN)


def PrintOrange(text):
    PrintColor(text, CommandLineColors.WARNING)


def PrintRed(text):
    PrintColor(text, CommandLineColors.FAIL)


def PrintBold(text):
    PrintColor(text, CommandLineColors.BOLD)


def PrintUnderline(text):
    PrintColor(text, CommandLineColors.UNDERLINE)


def PrintHeaderAndLog(text):
    PrintColorAndLog(text, CommandLineColors.HEADER)


def PrintBlueAndLog(text):
    PrintColorAndLog(text, CommandLineColors.OKBLUE)


def PrintGreenAndLog(text):
    PrintColorAndLog(text, CommandLineColors.OKGREEN)


def PrintOrangeAndLog(text):
    PrintColorAndLog(text, CommandLineColors.WARNING)


def PrintRedAndLog(text):
    PrintColorAndLog(text, CommandLineColors.FAIL)


def PrintBoldAndLog(text):
    PrintColorAndLog(text, CommandLineColors.BOLD)


def PrintUnderlineAndLog(text):
    PrintColorAndLog(text, CommandLineColors.UNDERLINE)
