#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

debug = False

directionPin = 17
pulsePin = 4
buttonInputPin = 22
buttonLightPin = 10
ghostOutputRelayPin = 7
skullOutputRelayPin = 6
lightOutputRelayPin = 27
CW = 1
CCW = 0

def turnTable(direction, duration):
    time.sleep(0.6)
    GPIO.output(directionPin, direction)
    time.sleep(0.6)

    # move counter-clockwise for x microseconds? - should already be set to clockwise at this point.
    for i in range(duration):
        GPIO.output(pulsePin, GPIO.LOW)
        GPIO.output(pulsePin, GPIO.HIGH)
        time.sleep(0.0006)


GPIO.setmode(GPIO.BCM)
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(pulsePin, GPIO.OUT)
GPIO.setup(ghostOutputRelayPin, GPIO.OUT)
GPIO.setup(skullOutputRelayPin, GPIO.OUT)
GPIO.setup(lightOutputRelayPin, GPIO.OUT)
GPIO.setup(buttonLightPin, GPIO.OUT)
GPIO.setup(buttonInputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(directionPin, CCW)
GPIO.output(buttonLightPin, GPIO.HIGH)


# simple test of all outputs
GPIO.output(ghostOutputRelayPin, GPIO.LOW) # the relay board expects low to be on
GPIO.output(skullOutputRelayPin, GPIO.LOW)
GPIO.output(lightOutputRelayPin, GPIO.LOW)
GPIO.output(buttonLightPin, GPIO.LOW)
time.sleep(1)
GPIO.output(ghostOutputRelayPin, GPIO.HIGH)
GPIO.output(skullOutputRelayPin, GPIO.HIGH)
GPIO.output(lightOutputRelayPin, GPIO.HIGH)
GPIO.output(buttonLightPin, GPIO.HIGH)

try:
    # loop
    while(1):
        # check if button triggered
        if GPIO.input(buttonInputPin) == GPIO.HIGH:
            if debug:
                print("button pressed")
            GPIO.output(skullOutputRelayPin, GPIO.LOW)
            GPIO.output(lightOutputRelayPin, GPIO.LOW)
            GPIO.output(buttonLightPin, GPIO.LOW)
            
            turnTable(CCW, 3500)
            
            GPIO.output(ghostOutputRelayPin, GPIO.LOW)
            
            turnTable(CW, 1500)
            
            GPIO.output(ghostOutputRelayPin, GPIO.HIGH)
            GPIO.output(skullOutputRelayPin, GPIO.HIGH)
            
            time.sleep(10) # set a timeout so you can't immediately press the button again.
            
            GPIO.output(lightOutputRelayPin, GPIO.HIGH)
            GPIO.output(buttonLightPin, GPIO.HIGH)
        else :
            if debug:
                print("button not pressed")
        time.sleep(0.06)
        
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()



GPIO.cleanup()