#!/usr/bin/python3
import paramiko
from AaSystem.LogAndPrint.Log import PrintAndLog, PrintRedAndLog, PrintBlueAndLog
from Agent.CommandInterface.ICommand import ICommand


class RemoteSSH(ICommand):
    def Execute(self):
        if self.CheckHelpRequested():
            return
        if self.CheckMinimunRequiredParameters(4):
            return
        hostname = self.request[0]
        port = self.request[1]
        username = self.request[2]
        password = self.request[3]
        commands = None if len(self.request) <= 4 else self.request[4:]

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=hostname, port=port, username=username, password=password)
            PrintBlueAndLog(f"Successfully established ssh connection to {hostname}")
            if commands and len(commands) > 0:
                for command in commands:
                    PrintAndLog(f"Running command remotely: {command}")
                    stdin, stdout, stderr = client.exec_command(command)
                    output = stdout.read().strip().decode().splitlines()
                    responseText = "Command Executed, remote machine response:\n"
                    for line in output:
                        responseText = f"{responseText}\n" \
                                       f"       {line}"
                    PrintAndLog(f"{responseText}\n")
        except Exception as ex:
            PrintRedAndLog(f"Failed attempting to connect to remote host, exception encountered:\n"
                           f"       {ex}\n")
        finally:
            PrintBlueAndLog(f"Finished running commands, close connection")
            client.close()

    def HelpRequested(self):
        PrintAndLog("\n"
                    "       Connects a remote machine via an ssh connection\n"
                    "       Command parameters: [hostname] [port] [username] [password] [command] [command] [command]\n"
                    "                     'hostname' - The address of the machine you are attempting to connect to\n"
                    "                     'port' - The port the connection will be made on\n"
                    "                     'username' - The username used in the connection request\n"
                    "                     'password' - The password used in the connection request\n"
                    "                     'command' - A list of linux shell commands wrapped in parentheses, each "
                    "command will be run in turn once a connection is established to the remote machine\n")


RemoteSSH.PublicFacing = "ssh"
