import sys
from venv.AttackAgent.Bash.BashCommands import Bash


class AttackAgentMain:
    def __init__(self):
        self.AvailableCommands = ["--help", "-ba"]

    def CreateRequest(self, userInput):
        return str.split(userInput, ' ')

    def WaitForInput(self):
        print("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information")
        while True:
            userInput = input("Please enter your next command, type help for options\n")
            request = self.CreateRequest(userInput)
            self.PerformRequest(request)

    def HelpRequested(self):
        print(str.join(', ', self.AvailableCommands))

    def CheckAvailableCommand(self, userInput):
        if not userInput in self.AvailableCommands:
            print("No such command")
            return False
        return True

    def PerformRequest(self, request):
        command = str.lower(request[0])
        print(command)
        if not self.CheckAvailableCommand(command):
            return
        if command == "--help":
            self.HelpRequested()
        if command == "-ba":
            Bash().RunBashCommand(request)


if len(sys.argv) > 1:
    AttackAgentMain().PerformRequest(sys.argv[1:])
elif __name__ == '__main__':
    attackAgent = AttackAgentMain()
    attackAgent.WaitForInput()
