
Linux Command list:

#log viewing on command line

	$ tail -f   <file name>

#find the process id (pid) for python scripts that are running
 	ps -ef | grep python
 
 	Result <pid>= 14764::  "root 14764 14757  0 Jun21 pts/0    00:00:00 python HWcontrolServer.py"


#softly kill the script or process:
 	kill -TERM <pid>

#Hard Kill the script or process:
 	kill -KILL <pid>
 	"-KILL = -9"

#Other
 	mkdir <file name>

#GitHub
	$ man git  #manual command
	git clone git@github.com:Bendito62/GitHub_Python-scripts.git
	https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

	git clone <repository location>
	
	git add <files to add to repository>
	git commit -m
	git status
	git pull <automatically merges repository with local code>
	git checkout <branch name>  #switch to a new branch
	
	

#GitHub ssh:
	
	ls ~/.ssh  #look for ssh keys
	https://help.github.com/articles/generating-ssh-keys/ #tutorial
	