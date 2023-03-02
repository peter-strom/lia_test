import settings

def get_uart():
    line = ser.readline()
    #line = ser.read_until('\n')
    #ser.reset_input_buffer()
    #print (line)
    if line:
        line = line.decode()
        return line
    
def get_uart_from_irq_toggle(button):
    button.toggle()
    uart_msg = get_uart()
    if uart_msg:
        return uart_msg