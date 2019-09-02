#!/usr/bin/python3
import multiprocessing
from AaSystem.LogAndPrint.Log import PrintRedAndLog


Processes = {}


def RunProcess(request):
    print("running!")
    # if processName in Processes:
    #     PrintRedAndLog(f"Process {processName} is an active process. Cannot run multiple processes by the same name.")
    #     return
    # newProcess = multiprocessing.Process(target=func)
    # Processes[processName] = newProcess
    # newProcess.start()


def StopProcess(request):
    print("stopping!")
    # if processName in Processes:
    #     Processes[processName].terminate()


def GetProcess(request):
    print("getting!")
    # if processName in Processes:
    #     return Processes[processName]


def WaitForProcess(request):
    print("waiting!")
    # try:
    #     if processName in Processes:
    #         Processes[processName].join()
    # except Exception as ex:
    #     print(f"Failed waiting for process, exception encountered:\n")
    #     PrintRedAndLog(ex)


RunProcess.PublicFacing = "runProcess"
StopProcess.PublicFacing = "stopProcess"
GetProcess.PublicFacing = "getProcess"
WaitForProcess.PublicFacing = "waitProcess"
