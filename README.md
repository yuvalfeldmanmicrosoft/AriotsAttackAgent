## Ariots Attack Agent

## Overview
The Attack Agent is a "red team" tool for testing and automating attacks on our system under the assumption that we are starting from within an IoT device - that we have already breached the first device and have and agent installed on it.

The Attack Agent is meant to make it simple and accessible to activate attack scenarios which will test our alerting and defensive capabilities. The agent is still in development and will be updated with new capabilities and scripted scenarios according to need.

At any point you can type -help to get additional information on the available functions and the purpose of those functions and commands.

***please note that the attack agent is not a finished product. Additional features and capabilities can be requested and bugs may be found (in case bugs are found please do not disturb them).


##Activation
The attack agent can be called either by activating it - in this case it will turn on, display a welcome message and wait for user input or by calling it via command line and passing the input as added arguments. For example:
	* Activating the attack agent and then passing commands:
		a. attackagent
		b. getip
	* Calling the attack agent via command line:
		a. attackagent getip

Additional information:
	* Many commands can be linked one after the other to form more complex commands. (i.e.: asynch loop 12 ping self will open a new process and call ping localhost on it 12 times.)
	* The Attack agent has a command queue, all commands will be added to the queue according to their run order and activated one at a time.
	* The Attack agent is written in python.
	* The Attack agent supports calling -help from all steps of the way to get more information on the available functions and what those functions do.
	* The Attack agent requires an environment variable to be set up in order to run (see Installation for more information)
	* All commands being run will be logged shown on the CLI and all commands being run will be called on the CLI before they are activated - currently no long term logging exists but it may be added later on if there it is needed.
	





##Installation
To install run the following in the command line (currently automated installation using this function is available only on Linux machines):

```
cd /home;sudo git clone https://github.com/yuvalfeldmanmicrosoft/AriotsAttackAgent.git;cd AriotsAttackAgent/;sudo chmod +x AttackAgent.py;sudo mkdir -p ~/bin;sudo cp -s /home/AriotsAttackAgent/AttackAgent.py ~/bin/attackagent;sudo echo 'export PATH="$PATH:~/bin:AriotsAttackAgent=ON"' >> ~/.bashrc;cd $HOME;source ~/.bashrc;
```


***Please note we have currently added an Agent Shield that will help protect from unwanted or accidental activation of the agent on a machine. On activation the agent will search for the environment variable AriotsAttackAgent=ON, if the machine doesn’t have this variable the attack agent will not run.



##Upgrading
Upgrading the Attack Agent after installation can be do>ne by passing it the upgrade command (via the cli):

```
attackagent upgrade
```



Testing develop
```
sudo mkdir -p ~/bin;cd /home;sudo git clone https://github.com/yuvalfeldmanmicrosoft/AriotsAttackAgent.git;cd AriotsAttackAgent;sudo git checkout develop;cd AriotsAttackAgent/;sudo chmod +x AttackAgent.py;sudo cp -s /home/AriotsAttackAgent/AttackAgent.py ~/bin/attackagent;sudo echo 'export PATH="$PATH:~/bin:AriotsAttackAgent=ON"' >> ~/.bashrc;cd $HOME;source ~/.bashrc;
```




##Alerts

Alert commands run simple custom bash code snippets targeted at raising IoT alerts. 
Bash commands are:

###Administrative Alerts:
```
Command Name 				Command	Triggers Alert				Comment
Add Suspicious User			addsuspicioususer				IOT_AddSuspiciousUser	
Privileged Container			privilegedcontainer				IOT_PrivilegedContainer	
Disable Audited Logging			disableauditdlogg				IOT_DisableAuditdLogging	
Suspicious Nohup			suspiciousnohup 				IOT_SuspiciousNohup	
```

###Change machine files and settings Alerts:
```
Command Name 				Command	Triggers Alert				Comment
Removal Of System Logs			removelofsystemlogs				IOT_RemovelOfSystemLogs	
Ransomware				ransomware					IOT_Ransomware	
Override Linux Files			overridelinuxfiles				IOT_OverrideLinuxFiles	
Linux Back door				linuxbackdoor					IOT_LinuxBackdoor	
Fairware Malware			fairwaremalware					IOT_FairwareMalware	
Egress Data				egressdata					IOT_EgressData	
Disable Firewall			disablefirewall					IOT_DisableFirewall	
Common Bots				commonbots					IOT_CommonBots	
```

###File Retrieval Alerts:
```
Command Name 				Command	Triggers Alert				Comment
Download File Then Run			downloadfilethenrun				IOT_DownloadFileThenRun	
Crypto Miner				cryptominer					IOT_CryptoMiner	
Download Virus File			downloadvirusfile		
Possible Malware			possiblemalware					IOT_PossibleMalware	
```

###Information Retrieval Alerts:
```
Command Name 				Command	Triggers Alert				Comment
Linux Reconnaissance			linuxreconnaissance				IOT_LinuxReconnaissance	
Clear History File			clearhistoryfile				IOT_ClearHistoryFile	
```

###Process and ports Alerts:
```
Command Name 				Command	Triggers Alert				Comment
Reverse Shell Alert			reverseshellalert				IOT_ReverseShell	
```



##Bash commands

Bash commands run simple bash code snippets. They are the basis for larger scenarios and attacks and are normally used to create the larger scenarios.
Bash commands are:

###Administrative commands:
```
Command Name 				Command						Command activity 							Comment
Add User				adduser						Adds a new user to the machine						Can be added as a regular user, as an admin or as part of a group
Change User Password			changeuserpassword				Updates a user's password	
```

###Commands that alter files and settings:
```
Command Name 				Command						Command activity 							Comment
Delete Files				deletefiles					Deletes files or folders on the machine					Can be called so it deletes a single file or directory or an entire directory recursively
Create File				createfile					Can create a new empty file or directory				Can be called so it creates an empty file, a file on the d-bus or a directory
Copy File				copyfile					Copies a file or directory	
```

###Custom commands:
```
Command Name 				Command						Command activity 							Comment
Perform Custom Command			custombash					Performs a custom bash command	
```

###File Retrieval commands:
```
Command Name 				Command						Command activity 							Comment
Git Clone				gitclone					Clones a git repository							Can add a path parameter to set a clone location
Download File				downloadfile					Uses wget to download a file	
Retrieve File				retrievefile					Uses a curl command to add file content to the terminal	
```

###Information Retrieval commands:
```
Command Name 				Command						Command activity 							Comment
Ip Config				getip						Gets the current machines IP information				One of the only actions that works on both Linux and Windows machines - also used as a sanity test that things are running
Who Am I				whoami						Runs the self-discovering command whoami	
Ping					ping						Pings a destination							Can be used to automatically ping google, localhost, 8.8.8.8 or a custom destination
```

###Process and ports commands:
```
Command Name 				Command						Command activity 							Comment
Stop Service				reverseshell					Stops a service by name	
Reverse Shell				killprocess					Performs the bash command: 'python import socket' on a provided path	
Kill Process				stopservice					Kills a process								Can be called to kill by process on port, by process name, by partial process name or by processID
```



##Scenario commands


Scenario commands are meant to "run" scenarios - also known as batch commanding (running multiple commands in sequence). 
The scenario command name is: run

Run has two modes:

	* Premade scenarios - Run uses premade scenarios that are saved to the attack agent to run specific scenarios that are useful or used often by running the command and then calling the scenario name - additional scenarios can be created and added to the premade scenario directory by contacting the agent admins and requesting the be added. Once a scenario has been added to the agents scenario pool it will be accessible on every installation and upgrade of the agent.
	***Currently we are working on creating the first scenarios - once we build them the One note will be updated, in addition at any time you can see the existing scenarios by calling -help on the run command (i.e.: attackagent run -help) to get a list of all the premade available scenarios
	Premade scenario example - attackagent run attackscenario1
	* Custom scenario files -  Custom scenarios can be created by creating a scenario file -  a text file with commands separated by line breaks and calling the run command with the custom URL parameter followed by the URL to the file: attackagent run -c "my\full\path\mycustomscenariofile.txt"


More information on creating custom scenarios
	* All custom scenarios will be executed in order line by line
	* A line can be commented out by adding the # character to the beginning of the line
	* Scenarios can be added recursively by adding a call custom or premade scenario command as a line inside a scenario - in such a case the scenario being run recursively will run to completion before the parent scenario is resumed.


```
Typing run -help will show all the Premade scenarios currently available.
```


*Scenarios can be easily added to the premade scenario pool, if you have a scenario you use offer or feel can aid others or simply feel should be added please contact one of the product owners and we will add it to the default pool
*I am working on adding a remote scenario pool, when that is ready you will be able to add your scenario to a remote open service and run the command via that scenario pool



##System commands


These commands are aimed at supporting scenarios and provide a set of tools to "programmatically" order and handle calling scenario commands.

The current available system commands are:

```
Command Name 			Command							Command activity 							Comment
Wait				wait							Waits the process for a designated amount of time			The wait can be activated in a timespan of seconds, minutes, hours and days
Loop				Loop							Repeats a provided command X times	
ForEach				foreach							Allows dynamic replacing of parts of commands with a list of options	A number of different parts of the command can be replaced in a single call
Asynch Foreach			asyncforeach						Like Foreach but all the commands generated run async	
Run Process			async							Runs the provided command on a new process				All commands added via that command will also run on that new process in their own CommandQueue
Run Process pool		asyncpool						Runs a list of provided commands each in its own process		Each command will get its own process and its own CommandQueue
```



##Remote Connection Commands

These commands are aimed at Connecting to remote machines, pinging, sniffing and performing actions involving other machines

The current available remote commands are:

```
Command Name 			Command							Command activity 												Comment
Remote SSH			ssh							Will create a remote ssh connection with a target machine and performs shell commands as provided		The connection is made on hostname and port using a username and password. Once the connection is made (if it is made successfully) the command also permits passing additional commands to run on the remote machine
Migrate And Perform Commands	migrate							Will create a remote ssh connection, install the attack agent and perform shell commands on the machine	
```


***There is a known issue currently where after installing an attack agent on a remote machine and calling commands on it the result will not be returned to be displayed on the calling machines terminal even though the command had been executed successfully 



##Logging

```
Due to an issue with permissions, logs have been temporarily disabled
```

All actions performed be the agent and all outputs, inputs and data collected will be stored in a local log under .\agentDirectory\Logs\{AttackAgent[day][month][year]}.txt
These logs currently do not support crash dumps.

Log example:
After turning on the AttackAgent and performing a series of calls I could then find under the file .\AttackAgentLocalDirectory\AttackAgentLog1182019.txt containing the logs:
```

			2019-08-11 14:03:33.739799: Operating system detected: windows
			2019-08-11 14:03:33.740800: Hello, Welcome to the Linux based ArIoTS Attack Agent. Type --help at any stage for more information
			2019-08-11 14:03:38.238760: User input: asd
			2019-08-11 14:03:38.240762: No such command 'asd'
			2019-08-11 14:03:40.359686: User input: -help
			2019-08-11 14:03:40.361685: All commands follow the format - [CommandType] [CommandsParameter] [CommandsParameter] ...
			Type -help with any CommandType for more information on that command
			
			Available CommandsTypes:
			ba: Bash Attacks using bash commands to perform tasks
			run: References text files containing a row delimited list of commands to run, places these commands at the front of the queue
			sc: Attack Agent System Commands - will perform program and environment commands such as waiting, looping, handling environment variables and so on
			upgrade: Upgrades to latest version of Ariots Attack Agent - currently only supported on linux machines
			2019-08-11 14:03:43.238376: User input: ba
			2019-08-11 14:03:43.240343: Running Command:    ba
			2019-08-11 14:03:43.242375: No Bash command to execute passed in parameters
			2019-08-11 14:03:45.198918: User input: ba -help
			2019-08-11 14:03:45.200917: Running Command:    ba -help
			2019-08-11 14:03:45.202918: Command parameters: ba [BashCommand]
			ba: stands for Bash Attack. ba commands run bash code aimed at triggering alerts supporting larger attack functions
			     'BashCommand' - The type of Bash Command that will be run
			     Possible BashCommands:
			            getip
			            addsuspicioususer
			            suspiciousnohup
			            reverseshell
			            removelofsystemlogs
			            ransomware
			            privilegedcontainer
			            possiblemalware
			            overridelinuxfiles
			            linuxreconnaissance
			            linuxbackdoor
			            fairwaremalware
			            egressdata
			            downloadfilethenrun
			            disablefirewall
			            disableauditdlogg
			            cryptominer
			            commonbots
			            clearhistoryfile
			It is also possible to pass your own bash code by passing the argument -c and then the code in parentheses, i.e.: attackagent ba -c 'ipconfig'
			For more information on a command add -help after a command, i.e.: 'ba getip -help'
			2019-08-11 14:03:49.226702: User input: ba getip -help
			2019-08-11 14:03:49.228703: Running Command:    ba getip -help
			2019-08-11 14:03:49.230202: Performs the bash command: 'ipconfig'
			Meant as a simple code functionality and sanity test
			2019-08-11 14:03:52.566879: User input: ba getip
			2019-08-11 14:03:52.572374: Running Command:    ba getip
			2019-08-11 14:03:52.574414: Running shell command: ipconfig
			2019-08-11 14:03:52.709144: 
			
			Windows IP Configuration
```

	

			

