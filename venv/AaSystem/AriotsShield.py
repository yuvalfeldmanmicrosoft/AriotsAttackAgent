#!/usr/bin/python3
from venv.AaSystem.Log import PrintRedAndLog, WriteToLog
from venv.AaSystem.SystemInspector import GetOperatingSystemName, GetEnvironmentVariableWindows, \
    GetEnvironmentVariableLinux


SupportedOsTypes = ["windows", "linux"]


def IsSupportedOs(OperatingSystem):
    if OperatingSystem not in SupportedOsTypes:
        PrintRedAndLog(f"Operating system: '{OperatingSystem}' not supported")
        return False
    return True


def HasAriotsEnvironmentVariable(OperatingSystem):
    if OperatingSystem == "windows":
        return GetEnvironmentVariableWindows('AriotsAttackAgent') == "ON"
    return "AriotsAttackAgent=ON" in GetEnvironmentVariableLinux("PATH")


def RunningOnPermittedMachine():
    OperatingSystem = str.lower(GetOperatingSystemName())
    WriteToLog(f"Operating system detected: {OperatingSystem}")
    PermittedToRunOnMachine = IsSupportedOs(OperatingSystem) and HasAriotsEnvironmentVariable(OperatingSystem)
    return PermittedToRunOnMachine
