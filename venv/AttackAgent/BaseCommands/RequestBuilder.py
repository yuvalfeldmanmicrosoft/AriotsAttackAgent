#!/usr/bin/python3
import shlex


def ParseRequest(userInput):
    return shlex.split(userInput)