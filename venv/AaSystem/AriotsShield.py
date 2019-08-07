#!/usr/bin/python3
from venv.AaSystem.Colors import PrintRed
from venv.AaSystem.SystemInspector import GetOperatingSystemName, GetEnvironmentVariableWindows, \
    GetEnvironmentVariableLinux


SupportedOsTypes = ["windows", "linux"]


def IsSupportedOs(OperatingSystem):
    if OperatingSystem not in SupportedOsTypes:
        PrintRed(f"Operating system: '{OperatingSystem}' not supported")
        return False
    return True


def HasAriotsEnvironmentVariable(OperatingSystem):
    if OperatingSystem == "windows":
        return GetEnvironmentVariableWindows('AriotsAttackAgent') == "ON"
    return "AriotsAttackAgent=ON" in GetEnvironmentVariableLinux("PATH")


def RunningOnPermittedMachine():
    OperatingSystem = str.lower(GetOperatingSystemName())
    PermittedToRunOnMachine = IsSupportedOs(OperatingSystem) and HasAriotsEnvironmentVariable(OperatingSystem)
    return PermittedToRunOnMachine
