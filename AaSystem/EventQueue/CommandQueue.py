#!/usr/bin/python3
import queue


commandQueue = "commandQueue"
tempQueue = "tempQueue"


CommandQueues = {
    "main": {
        commandQueue: queue.Queue(),
        tempQueue: queue.Queue()
    }
}


def CreateNewCommandQueueIfNonExist(queueName):
    if queueName in CommandQueues:
        return
    newQueue = {
        commandQueue: queue.Queue(),
        tempQueue: queue.Queue()
    }
    CommandQueues[queueName] = newQueue


def CommandQueueNotEmpty(queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    return not CommandQueues[queueName][commandQueue].empty()


def EnqueueCommand(command, queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    CommandQueues[queueName][commandQueue].put(command)


def EnqueueCommands(commands, queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    for command in commands:
        CommandQueues[queueName][commandQueue].put(command)


def EnqueueCommandsNext(commands, queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    while not CommandQueues[queueName][commandQueue].empty():
        CommandQueues[queueName][tempQueue].put(CommandQueues[queueName][commandQueue].get())
    for command in commands:
        CommandQueues[queueName][commandQueue].put(command)
    while not CommandQueues[queueName][tempQueue].empty():
        CommandQueues[queueName][commandQueue].put(CommandQueues[queueName][tempQueue].get())


def DeQueueCommand(queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    if CommandQueueNotEmpty():
        return CommandQueues[queueName][commandQueue].get()
    else:
        return None


def EmptyCommandQueue(queueName="main"):
    CreateNewCommandQueueIfNonExist(queueName)
    while not CommandQueues[queueName][commandQueue].empty():
        CommandQueues[queueName][commandQueue].get()
