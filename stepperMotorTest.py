#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

directionPin = 20
pulsePin = 16
inputPin = 2
CW = 1
CCW = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(pulsePin, GPIO.OUT)
GPIO.setup(inputPin, GPIO.IN)
GPIO.output(directionPin, CCW)


#while(1):
    # put your main code here, to run repeatedly:

    # check if button triggered
    #if GPIO.input(inputPin) == GPIO.HIGH:

# move clockwise for x microseconds? - should already be set to clockwise at this point.
for i in range(5000): # 50000 x 60 microseconds ~= 3 seconds
    GPIO.output(pulsePin, GPIO.LOW)
    GPIO.output(pulsePin, GPIO.HIGH)
    time.sleep(0.00006)


# Change Direction CounterClockWise: Changing direction requires time to switch. The time is dictated by the stepper motor and controller.
time.sleep(0.6)
GPIO.output(directionPin, CW)
time.sleep(0.6)

# move counter-clockwise for x microseconds? - should already be set to clockwise at this point.
for i in range(1000):
    GPIO.output(pulsePin, GPIO.LOW)
    GPIO.output(pulsePin, GPIO.HIGH)
    time.sleep(0.00006)


# Change Direction CLockwise: Changing direction requires time to switch. The time is dictated by the stepper motor and controller.
time.sleep(0.6)
GPIO.output(directionPin, CCW)
time.sleep(0.6)
        
    #time.sleep(1)




GPIO.cleanup()