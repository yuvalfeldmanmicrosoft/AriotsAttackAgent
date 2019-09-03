#!/usr/bin/python3


InstallationShellScript = "cd /home;sudo git clone https://github.com/yuvalfeldmanmicrosoft/AriotsAttackAgent.git;" \
                          "cd AriotsAttackAgent/;sudo chmod +x AttackAgent.py;sudo mkdir -p ~/bin;sudo cp -s " \
                          "/home/AriotsAttackAgent/AttackAgent.py ~/bin/attackagent;sudo echo 'export " \
                          "PATH=\"$PATH:~/bin:AriotsAttackAgent=ON\"' >> ~/.bashrc;cd $HOME;source ~/.bashrc;"
