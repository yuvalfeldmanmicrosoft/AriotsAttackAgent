#!/usr/bin/python3
from AaSystem.Context.Context import Context
from AaSystem.EventQueue.CommandQueueFactory import GetCommandQueue


def GetContext():
    commandQueue = GetCommandQueue()
    context = Context(commandQueue)
    commandQueue.SetContext(context)
    return context
