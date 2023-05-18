from machine import UART, Pin
import dht
import utime

uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,timeout=500)
# setting GPIO Pin 
sensor = dht.DHT22(Pin(25))  # GPIO25 

def reading_sensor():
    sensor.measure()
    temp_str = "Temp: {0:3.1f}".format(sensor.temperature())
    humi_str = "Humi: {0:3.1f}".format(sensor.humidity())
    # set text display
    uart.write(temp_str)
    uart.write("/")
    uart.write(humi_str)
    
while(1):
    reading_sensor()
    utime.sleep(5)