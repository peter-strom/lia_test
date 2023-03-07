import serial
import uart

uart = uart.init()

def get_uart():
    line = uart.readline()
    #line = uart.read_until('\n')
    #uart.reset_input_buffer()
    #print (line)
    if line:
        line = line.decode()
        return line
    
def get_uart_from_irq_toggle(button):
    button.toggle()
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg