
#import functions as f
import serial
import time
from gpiozero import OutputDevice,InputDevice, Button
import unittest
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

ser = serial.Serial(
        port='/dev/ttyS0', # gpio pin 8 and 10 (raspi-config)
        #port='/dev/ttyACM0', # USB
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.1
)

def get_uart():
    line = ser.readline()
    if line:
        line = line.decode()
        return line
    
def get_uart_from_irq_toggle(button):
    button.toggle()
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg
    else:
        return "none"
        



class Test(unittest.TestCase):

    #GIVEN irq not active WHEN activate irq THEN execute right callback function.
    def test_irq_off_1on(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_off), 'EXTI_CALLBACK: SHUTDOWN \r\n')
    
    def test_irq_power_supply_1on(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_irq_sensor_1on(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_sensor), 'EXTI_CALLBACK: SENSOR ALARM \r\n')

    def test_irq_sreset_update_1on(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_sreset_update), 'EXTI_CALLBACK: RESET / UPDATE \r\n')

    def test_irqn_usbc_1on(self):
        self.assertEqual(get_uart_from_irq_toggle(irqn_usbc) , 'EXTI_CALLBACK: USBC \r\n')

       #GIVEN irq active WHEN deactivate irq THEN execute right callback function.
    def test_irq_off_2off(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_off), 'none')
    
    def test_irq_power_supply_2off(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_irq_sensor_2off(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_sensor), 'none')

    def test_irq_sreset_update_2off(self):
        self.assertEqual(get_uart_from_irq_toggle(irq_sreset_update), 'none')

    def test_irqn_usbc_2off(self):
        self.assertEqual(get_uart_from_irq_toggle(irqn_usbc) , 'none')





if __name__ == '__main__':
    unittest.main()