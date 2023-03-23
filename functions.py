import serial
import uart
import time

uart = uart.init()



def send_uart(buff):
    uart.write(buff)

def get_uart():
    line = uart.readline()
    #line = uart.read_until('\n')
    #uart.reset_input_buffer()
    #print (line)
    if line:
        line = line.decode()
        return line
def trigger_sensor_irq():
    send_uart("3".encode())
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg

def untrigger_sensor_irq():
    return None

def get_uart_from_irq_toggle(button):
    uart.reset_input_buffer()
    button.toggle()
    time.sleep(0.1)
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg

def get_uart_from_long_press(button,time_s):
    uart.reset_input_buffer()
    button.toggle()
    time.sleep(time_s)
    button.toggle()
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg