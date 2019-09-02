import inspect
import sys


def GetFunctionsFromPath(filePath):
    return inspect.getmembers(sys.modules[filePath], inspect.isfunction)


def GetFunctionsWithAttributeFromPath(filePath, attribute):
    return [mem for mem in GetFunctionsFromPath(filePath) if hasattr(mem[1], attribute)]


def GetPublicFacingFunctionsFromPath(filePath):
    return GetFunctionsWithAttributeFromPath(filePath, "PublicFacing")
