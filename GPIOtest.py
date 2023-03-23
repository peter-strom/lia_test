
import functions as f
from testrig import Testrig
import unittest
import time

test_rig = Testrig
print("start")
time.sleep(1)
print("on")
test_rig.irq_off.on()
time.sleep(0.1)
print("off")
test_rig.irq_off.off()
time.sleep(1)
print("end")
class Test(unittest.TestCase):
    
    #GIVEN irq not active WHEN activate irq THEN call the right function.
    def test_01_GIVEN_on_WHEN_turn_on_all_outpins(self):
        f.send_uart("1".encode())
        time.sleep(0.1)
        self.assertTrue(test_rig.led_error.is_active)
        self.assertTrue(test_rig.led_on.is_active)
        self.assertTrue(test_rig.buzzer.is_active)
        self.assertTrue(test_rig.fan_control.is_active)
        self.assertTrue(test_rig.operation1.is_active)
        self.assertTrue(test_rig.operation2.is_active)
        self.assertTrue(test_rig.operation3.is_active)
        f.send_uart("0".encode())
        time.sleep(0.1)
        self.assertFalse(test_rig.led_error.is_active)
        self.assertFalse(test_rig.led_on.is_active)
        self.assertFalse(test_rig.buzzer.is_active)
        self.assertFalse(test_rig.fan_control.is_active)
        self.assertFalse(test_rig.operation1.is_active)
        self.assertFalse(test_rig.operation2.is_active)
        self.assertFalse(test_rig.operation3.is_active)
        f.send_uart("2".encode())
        time.sleep(0.1)
        self.assertTrue(test_rig.led_on.is_active)
       
    

if __name__ == '__main__':
    unittest.main()
