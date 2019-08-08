#!/usr/bin/python3
import platform
import os


def GetEnvironmentVariableWindows(variableName):
    return os.getenv(variableName)


def GetEnvironmentVariableLinux(variableName):
    return os.environ[variableName]


def GetOperatingSystemName():
    return platform.system()


def GetOperatingSystemRelease():
    return platform.release()


def GetOperatingSystemVersion():
    return platform.version()
