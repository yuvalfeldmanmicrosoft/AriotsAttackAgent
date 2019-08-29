#!/usr/bin/python3
import subprocess
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog, PrintBlueAndLog


def RunSubProcess(commandLineInput):
    try:
        PrintBlueAndLog(f"Running shell command: {commandLineInput}")
        result = subprocess.run(commandLineInput, shell=True, check=True, stdout=subprocess.PIPE)
        PrintAndLog(result.stdout.decode('utf-8'))
    except Exception as ex:
        PrintAndLog(f"Failed execute bash command '{commandLineInput}', exception encountered:\n")
        PrintRedAndLog(ex)
