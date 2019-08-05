from Colors import PrintRed
from venv.BaseCommandHandling.CommandQueue import EnqueueCommandsNext
import ntpath


def HelpRequested():
    print("Command parameters: -run [filePath]\n"
          "-run: References text files containing a row delimited list of commands to run, places these commands at "
          "the front of the queue\n"
          "     'filePath' - the full path to the batch command file"
          "     The batch file referenced will must contain only commands as provided when normally calling "
          "the attack agent\n"
          "     Each command must be separated by a new line\n"
          "     It is possible to recursively add additional batch -run calls using a batch file")


def AddCommandsBatch(request):
    if not request:
        PrintRed(f"Parameter PATH not provided in request")
        return
    filePath = request[0]
    if filePath == "-help":
        HelpRequested()
        return
    try:
        with open(filePath, "r") as file:
            commandLines = list(file.read().splitlines())
            print(f"Adding {len(commandLines)} Commands from {ntpath.basename(filePath)}")
            EnqueueCommandsNext(commandLines)
        file.close()
    except Exception as ex:
        print(f"Failed to load command batch file, exception encountered:\n")
        PrintRed(ex)
