
import time
from gpiozero import OutputDevice, InputDevice, Button

class Testrig:
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


