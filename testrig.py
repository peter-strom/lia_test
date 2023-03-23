
import time
from gpiozero import OutputDevice, InputDevice, Button

class Testrig:
    led_on = InputDevice("BOARD19",pull_up = None, active_state= True)
    buzzer = InputDevice("BOARD21",pull_up = None, active_state= True)
    fan_control = InputDevice("BOARD38",pull_up = None, active_state= True)
    led_error = InputDevice("BOARD23",pull_up = None, active_state= True)
    operation1 = InputDevice("BOARD26",pull_up = None, active_state= True)
    operation2 = InputDevice("BOARD24",pull_up = None, active_state= True)
    operation3 = InputDevice("BOARD22",pull_up = None, active_state= True)

    irq_power_supply = OutputDevice("BOARD37", active_high=True, initial_value=False)
    irq_off = OutputDevice("BOARD07", active_high=True, initial_value=False)
    irq_sreset_update = OutputDevice("BOARD03", active_high=True, initial_value=False)
    #irq_sensor = OutputDevice("BOARD12", active_high=True, initial_value=None)
    #irqn_usbc = OutputDevice("BOARD36", active_high=False, initial_value=None)
    irqn_mcu_reset = OutputDevice("BOARD05", active_high=False, initial_value=None)


