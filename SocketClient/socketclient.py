#!/usr/bin/env python3
#___________________________________________________________________________________
#
#Socket client example in python3.4
#
# to close the Socket client, type "exit" into the command line.  The server send back
# a string, "exiting !!!" and is captured by the program to initiate the exit.
#____________________________________________________________________________________


import socket   #for sockets
import sys  #for exit
import time

# Host Constants
host='192.168.1.110'       # Symbolic name meaning all available interfaces  
port = 8888
# Arbitrary non-privileged port

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + str(msg[1]))
    sys.exit();
 
print('Socket Created')

 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
     
print('Ip address of ' + host + ' Host is ' + remote_ip)
 
#Connect to remote server
s.connect((remote_ip , port))
 
print('Socket Connected to ' + host + ' Host on ip ' + remote_ip)

#Test initil data transfer to server
#Send some data to remote server
s.sendall(bytes('Socket Data Confirmation','UTF-8'))

print (s.recv(4096).decode('UTF-8'))
print (s.recv(4096).decode('UTF-8')) #windows python seems to require a second s.recv to handle back to back data from server

x=True
while x:
    #Receiving from client
    message =input('enter data:')
    if not message:
        message='Please Enter a Command'
    try :
        #Set the whole string
        s.sendall(bytes(message,'UTF-8'))
    except socket.error:
        #Send failed
        print('Send failed')
        sys.exit()
     
    print('Message send successfully')
    #time.sleep(.1)
    #Now receive data
    reply = s.recv(4096).decode('UTF-8')
     
    print(reply)
    if reply == 'exiting !!!':
        x=False
        
s.close()
