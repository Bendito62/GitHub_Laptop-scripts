#!/usr/bin/env python
#___________________________________________________________________________________
#
#Python2
#
#Kill Switch program for the raspberry pi controller.  Test 3 color LED with switch
#input to start kill switch countdown.  re-enter the LED sequence by pushing the
#button again.  The program is terminated by holding the switch down for >4 seconds.
#____________________________________________________________________________________


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

x=True
y=False
offLoop=True
timePB = 5

while x:
    GPIO.output(15, True)
    time.sleep(.1)
    GPIO.output(15, False)
#    time.sleep(1)
    

    GPIO.output(11, True)
    time.sleep(.1)
    GPIO.output(11, False)
  #  time.sleep(1)


    GPIO.output(13, True)
    time.sleep(.1)
    GPIO.output(13, False)
  #  time.sleep(1)

    pushB1=GPIO.input(16)                       #Look for Kill switch push
    if pushB1==False:
        offLoop = pushB1
        t=0
        while GPIO.input(16) == False:          #wait for Kill switch to be releaseased
            t=t+1                               #Count 1/10 seconds of held Kill swith 
            time.sleep(.1)

        if t >= 40:                             #Exit program after 4 seconds of a Held Kill switch
            y=False
            x=False
            offLoop = True
    
    if offLoop == False:
        time.sleep(1)
        if timePB == 0:
            print "Boooooom!!"
            y=True
            GPIO.output(11, False)              #clear LED ports to Off
            GPIO.output(13, False)
            GPIO.output(15, False)
        if timePB == 5:
            print "The kill switch has been activated! you have five seconds to escape! Komodo test"
        if (timePB <=5) and (timePB > 0):
            print timePB
            timePB= timePB-1

        while y:                                #wait for switch to be pushed again to re-enter LED sequence
            pushB1 = GPIO.input(16)
            if pushB1 == False:
                x=True
                y=False
                offLoop=True
                timePB=5
                print "starting over"
                
    
        
