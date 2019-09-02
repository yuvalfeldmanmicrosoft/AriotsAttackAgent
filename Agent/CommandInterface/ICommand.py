#!/usr/bin/python3
import abc
from AaSystem.LogAndPrint.Log import PrintRedAndLog


class ICommand(metaclass=abc.ABCMeta):
    def __init__(self, request, context):
        self.request = request
        self.context = context

    @abc.abstractmethod
    def Execute(self):
        pass

    @abc.abstractmethod
    def HelpRequested(self):
        pass

    def CheckHelpRequested(self):
        if "-help" in self.request:
            self.HelpRequested()
            return True
        return False

    def CheckMinimunRequiredParameters(self, min):
        if not self.request or len(self.request) < min:
            PrintRedAndLog("Missing required parameters")
            return True
        return False
