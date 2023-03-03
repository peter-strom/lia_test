
import functions as f
from testrig import Testrig
import unittest
import time

test_rig = Testrig

class Test(unittest.TestCase):

    #GIVEN irq not active WHEN activate irq THEN execute right callback function.
    def test_1_irq_off_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_off), 'EXTI_CALLBACK: SHUTDOWN \r\n')
    
    def test_1_irq_power_supply_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_1_irq_sensor_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sensor), 'EXTI_CALLBACK: SENSOR ALARM \r\n')

    def test_1_irq_sreset_update_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sreset_update), 'EXTI_CALLBACK: RESET / UPDATE \r\n')

    def test_1_irqn_usbc_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irqn_usbc) , 'EXTI_CALLBACK: USBC \r\n')

    #GIVEN irq active WHEN deactivate irq THEN execute right callback function.
    def test_2_irq_off_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_off), None)
    
    def test_2_irq_power_supply_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_2_irq_sensor_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sensor), None)

    def test_2_irq_sreset_update_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sreset_update), None)

    def test_2_irqn_usbce_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irqn_usbc) , None)


if __name__ == '__main__':
    unittest.main()
