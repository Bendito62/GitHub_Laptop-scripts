#!/usr/bin/env python3.2
#___________________________________________________________________________________
#
#HWcontrolServer in Python3
#
#
#Sends exit string of "exiting !!!" to the client.  The Client exits based off of received exit string
#____________________________________________________________________________________

import socket
import sys
import RPi.GPIO as GPIO
import time

#GPIO Output definition:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#GPIO Input definition:
GPIO.setup(16, GPIO.IN)

#default states:
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)

from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error,msg:
    print ("Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
    sys.exit()
     
print ("Socket bind complete")
 
#Start listening on socket
s.listen(10)
print ("Socket now listening")
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    
    conn.send ("OK...." + conn.recv(1024)+ "\n\n")
    #Sending message to connected client    
    conn.send("Welcome to the server. Type something and hit enter\n") #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        if data == 'exit':
            conn.sendall('exiting !!!')
            break
        elif not data: 
            conn.sendall('Enter Data')
            break
        elif data == '1':
            GPIO.output(15, True)
            time.sleep(.1)
            GPIO.output(15, False)
            #    time.sleep(1)
            conn.sendall('Green LED')
    
        elif data == '2':
            GPIO.output(11, True)
            time.sleep(.1)
            GPIO.output(11, False)
            #  time.sleep(1)
            conn.sendall('Blue LED')
        
        elif data == '3':
            GPIO.output(13, True)
            time.sleep(.1)
            GPIO.output(13, False)
            #  time.sleep(1)
            conn.sendall('Red LED')
            
        else:   
            reply = 'OK...' + data
            conn.sendall(reply)
       
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ("Connected with " + addr[0] + ":" + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
