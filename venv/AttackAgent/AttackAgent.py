from venv.AttackAgent.Bash.BashCommands import Bash


class AttackAgentMain:
    def __init__(self):
        self.AvailableCommands = ["--help", "ipconfig"]
        print("Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help for more information")

    def WaitForInput(self):
        while True:
            userInput = input("Please enter your next command, type help for options\n")
            self.PerformRequest(userInput)

    def HelpRequested(self):
        print(str.join(', ', self.AvailableCommands))

    def CheckAvailableCommand(self, userInput):
        if not userInput in self.AvailableCommands:
            print("No such command")
            return False
        return True

    def PerformRequest(self, userInput):
        splitUserInput = str.split(userInput, ' ')
        helpRequested = "--help" in splitUserInput
        command = str.lower(splitUserInput[0])

        if not self.CheckAvailableCommand(command):
            return
        if command == "--help":
            self.HelpRequested()
        if command == "ipconfig":
            Bash().RunBashCommand("IpConfig", helpRequested)


if __name__ == '__main__':
    attackAgent = AttackAgentMain()
    attackAgent.WaitForInput()
