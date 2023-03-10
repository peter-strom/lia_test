
import functions as f
from testrig import Testrig
import unittest
import time

test_rig = Testrig

class Test(unittest.TestCase):
    
    #GIVEN irq not active WHEN activate irq THEN call the right function.
    def test_01_GIVEN_unset_WHEN_irq_off_set(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_off), None)
    
    def test_01_GIVEN_unset_WHEN_irq_power_supply_set(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_power_supply), 'PSU: outlet mode\r\n')

    def test_01_GIVEN_unset_WHEN_irq_sensor_set(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sensor), 'sensor_alarm!\r\n')

    def test_01_GIVEN_unset_WHEN_irq_sreset_update_set(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sreset_update), 'sensor_reset!\r\n')

    def test_01_GIVEN_unset_WHEN_irqn_usbc_set(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irqn_usbc) , 'EXTI_CALLBACK: USBC \r\n')

    #GIVEN irq active WHEN deactivate irq THEN call the right function.
    def test_02_GIVEN_set_WHEN_irq_off_unset(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_off), None)
    
    def test_02_GIVEN_set_WHEN_irq_power_supply_unset(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_power_supply), 'PSU: battery mode\r\n')

    def test_02_GIVEN_set_WHEN_irq_sensor_unset(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sensor), None)

    def test_02_GIVEN_set_WHEN_irq_sreset_update_unset(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irq_sreset_update), None)

    def test_02_GIVEN_set_WHEN_irqn_usbce_unset(self):
        self.assertEqual(f.get_uart_from_irq_toggle(test_rig.irqn_usbc) , None)

    def test_03_GIVEN_update_mode_WHEN_reset_irq(self): #THEN alarm and change mode
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_sensor,0.05), "sensor_alarm!\r\n")
    def test_04_GIVEN_reset_mode_WHEN_sensor_irq(self): #THEN nothing
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_sensor,0.05), None)
    def test_05_GIVEN_reset_mode_WHEN_reset_irq(self): #THEN reset and change mode.
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_sreset_update,0.05), "sensor_reset!\r\n")
    def test_06_GIVEN_update_mode_WHEN_reset_irq(self): #THEN update and do not change mode
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_sreset_update,0.05), "update_settings!\r\n")
    
 
    #poweroff test
    def test_95_GIVEN_normal_WHEN_power_off_pushed_1_9s(self):
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_off,1.9), None)
    def test_95_GIVEN_normal_WHEN_power_off_pushed_2_0s(self):
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_off,2.0), "power_off!\r\n")
    def test_96_GIVEN_off_WHEN_trigger_irq_power_supply(self):
        self.assertEqual(f.get_uart_from_long_press(test_rig.irq_power_supply,0.05), None)

if __name__ == '__main__':
    unittest.main()
