#!/usr/bin/env python
import serial
import RPi.GPIO as GPIO
import time
import unittest

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(3, GPIO.OUT)
GPIO.output(3,GPIO.LOW)
ser = serial.Serial(
        port='/dev/ttyS0', # gpio pin 8 and 10 (raspi-config)
        #port='/dev/ttyACM0', # USB
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

print(ser.name)
try:
    while 1:
        line = ser.readline()
        if line:
            line = line.decode()
            print(line)
        '''
        if GPIO.input(26):
            print("Pin 26 is HIGH")
            GPIO.output(17,GPIO.HIGH)
        else:
            print("Pin 26 is LOW")
            GPIO.output(17,GPIO.LOW)
        '''    
        time.sleep(0.000001)
except KeyboardInterrupt: 
    GPIO.cleanup() # cleanup all GPIO
