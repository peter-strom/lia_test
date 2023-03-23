import serial
import time
def init():
    uart = serial.Serial(
            port='/dev/ttyS0', # gpio pin 8 and 10 (raspi-config)
            #port='/dev/ttyACM0', # USB
            baudrate = 115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.6
            )
    return uart