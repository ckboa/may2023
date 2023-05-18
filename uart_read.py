# import required modules
from machine import UART, Pin, SoftI2C
import time
import machine
import ssd1306

# Set up the UART object with the desired configuration
# Here, we're using UART2 with a baud rate of 9600, 8 data bits, no parity bit, 1 stop bit, and a timeout of 500ms.
uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1, timeout=500)
i2c = SoftI2C(scl=Pin(25), sda=Pin(26))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Main script
if __name__ == "__main__": 
    # Loop forever, reading from the UART Rx and printing any received data
    while True:
        oled.fill(0)
        uart_read = uart.read()
        #x = uart_read.split("/")
        if uart_read != None:
            #y = str(uart_read)
            x = uart_read.split(b'/')
            print(x[0])
            print(x[1])
            oled.text(x[0], 0, 0)
            oled.text(x[1], 0, 10)
            oled.show()
