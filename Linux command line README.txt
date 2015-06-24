
Linux Command list:

$ tail -f   "file name"

#find the process id (pid) for python scripts that are running
 ps -ef | grep python
 
 Result <pid>= 14764::  "root 14764 14757  0 Jun21 pts/0    00:00:00 python HWcontrolServer.py"


#softly kill the script or process:
 kill -TERM <pid>

#Hard Kill the script or process:
 kill -KILL <pid>
 "-KILL = -9"