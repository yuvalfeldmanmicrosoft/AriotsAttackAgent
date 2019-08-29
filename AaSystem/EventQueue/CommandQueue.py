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


def CommandQueueNotEmpty(queueName="main"):
    return not CommandQueues[queueName][commandQueue].empty()


def EnqueueCommand(command, queueName="main"):
    CommandQueues[queueName][commandQueue].put(command)


def EnqueueCommands(commands, queueName="main"):
    for command in commands:
        CommandQueues[queueName][commandQueue].put(command)


def EnqueueCommandsNext(commands, queueName="main"):
    while not CommandQueues[queueName][commandQueue].empty():
        CommandQueues[queueName][tempQueue].put(CommandQueues[queueName][commandQueue].get())
    for command in commands:
        CommandQueues[queueName][commandQueue].put(command)
    while not CommandQueues[queueName][tempQueue].empty():
        CommandQueues[queueName][commandQueue].put(CommandQueues[queueName][tempQueue].get())


def DeQueueCommand(queueName="main"):
    if CommandQueueNotEmpty():
        return CommandQueues[queueName][commandQueue].get()
    else:
        return None


def EmptyCommandQueue(queueName="main"):
    while not CommandQueues[queueName][commandQueue].empty():
        CommandQueues[queueName][commandQueue].get()
