#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
while True:
	GPIO.output(11, True)
	time.sleep(.1)
	GPIO.output(11, False)
	time.sleep(.1)
	input_value = True
         

	input_value = GPIO.input(12)
	if input_value == False:
		print "The button has been pressed."
		while input_value == False:
			input_value = GPIO.input(12)