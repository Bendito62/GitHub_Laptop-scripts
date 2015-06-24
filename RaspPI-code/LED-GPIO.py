#!/usr/bin/env python

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

    pushB1=GPIO.input(16)
    if pushB1==False:
            offLoop = pushB1
    
    if offLoop == False:
        time.sleep(1)
        if timePB == 0:
            print "Boooooom"
            y=True
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
        if timePB == 5:
            print "The kill switch has been activated! you have five seconds to live!"
        if (timePB <=5) and (timePB > 0):
            print timePB
            timePB= timePB-1

        while y:
            pushB1 = GPIO.input(16)
            if pushB1 == False:
                x=True
                y=False
                offLoop=True
                timePB=5
                time.sleep(.2)
                
    
        
