from machine import Pin, I2C
import ssd1306

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


oled = oled.text('Hello World ', 0, 0)
oled = oled.text('Hello CK!!!', 0, 10)
oled.show()
