#!/usr/bin/python3
import multiprocessing
from AaSystem.LogAndPrint.Log import PrintRedAndLog


Processes = {}


def RunProcess(processName, func):
    if processName in Processes:
        PrintRedAndLog(f"Process {processName} is an active process. Cannot run multiple processes by the same name.")
        return
    newProcess = multiprocessing.Process(target=func)
    Processes[processName] = newProcess
    newProcess.start()


def StopProcess(request):
    print("stopping!")
    # if processName in Processes:
    #     Processes[processName].terminate()


def GetProcess(processName):
    if processName in Processes:
        return Processes[processName]


def WaitForProcess(processName):
    try:
        if processName in Processes:
            Processes[processName].join()
    except Exception as ex:
        print(f"Failed waiting for process, exception encountered:\n")
        PrintRedAndLog(ex)


StopProcess.PublicFacing = "stop"
