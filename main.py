
import functions as f
import settings
import unittest

settings.init()
irq_power_supply.toggle()
'''
class Test(unittest.TestCase):

    #GIVEN irq not active WHEN activate irq THEN execute right callback function.
    def test_1_irq_off_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_off), 'EXTI_CALLBACK: SHUTDOWN \r\n')
    
    def test_1_irq_power_supply_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_1_irq_sensor_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_sensor), 'EXTI_CALLBACK: SENSOR ALARM \r\n')

    def test_1_irq_sreset_update_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_sreset_update), 'EXTI_CALLBACK: RESET / UPDATE \r\n')

    def test_1_irqn_usbc_on(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irqn_usbc) , 'EXTI_CALLBACK: USBC \r\n')

    #GIVEN irq active WHEN deactivate irq THEN execute right callback function.
    def test_2_irq_off_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_off), None)
    
    def test_2_irq_power_supply_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_power_supply), 'EXTI_CALLBACK: PSU\r\n')

    def test_2_irq_sensor_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_sensor), None)

    def test_2_irq_sreset_update_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irq_sreset_update), None)

    def test_2_irqn_usbce_off(self):
        self.assertEqual(f.get_uart_from_irq_toggle(irqn_usbc) , None)


# pause before finishing test script
'''
'''
    def test_7sleep(self):
        time.sleep(10)
        self.assertEqual('hej','hej')
'''

'''
if __name__ == '__main__':
    unittest.main()
    
'''