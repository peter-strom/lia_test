import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while 1:
        if GPIO.input(26):
            print("Pin 26 is HIGH")
            GPIO.output(17,GPIO.HIGH)
        else:
            print("Pin 26 is LOW")
            GPIO.output(17,GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt: 
    GPIO.cleanup() # cleanup all GPIO
