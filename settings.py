import serial
import time
from gpiozero import OutputDevice, InputDevice, Button

global usart
global led_on, buzzer, fan_control, led_error, operation1, operation2, operation3
global irq_power_supply, irq_off, irq_sreset_update, irq_sensor, irqn_usbc
def init():
    led_on = InputDevice("BOARD19")
    buzzer = InputDevice("BOARD21")
    fan_control = InputDevice("BOARD23")
    led_error = InputDevice("BOARD22")
    operation1 = InputDevice("BOARD24")
    operation2 = InputDevice("BOARD26")
    operation3 = InputDevice("BOARD28")

    irq_power_supply = OutputDevice("BOARD37")
    irq_off = OutputDevice("BOARD40")
    irq_sreset_update = OutputDevice("BOARD38")
    irq_sensor = OutputDevice("BOARD12")
    irqn_usbc = OutputDevice("BOARD36", active_high=False)
    print("test")
    usart = serial.Serial(
            port='/dev/ttyS0', # gpio pin 8 and 10 (raspi-config)
            #port='/dev/ttyACM0', # USB
            baudrate = 115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.1
            )