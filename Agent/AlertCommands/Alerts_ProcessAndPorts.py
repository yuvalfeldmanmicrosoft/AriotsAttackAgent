#!/usr/bin/python3
from AaSystem.LogAndPrint.Log import PrintAndLog


def ReverseShellAlert(request, context):
    if "-help" in request:
        Help_ReverseShellAlert()
        return

    context.EnqueueCommandsNext(f"reverseshell /bin/sh")


def Help_ReverseShellAlert():
    return PrintAndLog("\n"
                       "        Performs the bash command python import socket /bin/sh\n"
                       "        Triggers alert: ReverseShell\n")


ReverseShellAlert.PublicFacing = "reverseshellalert"
