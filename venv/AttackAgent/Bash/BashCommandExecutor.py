import subprocess


def RunSubProcess(commandLineInput):
    subprocess.run(commandLineInput, shell=True, check=True)
