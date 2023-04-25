#!/usr/bin/env python3
from gpiozero import Servo
from time import sleep
import socket


import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

print(get_ip_address())
RST = None
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_address=0x3C)

servo = Servo(18)

try:
	while True:
         servo.min()
         sleep(0.5)
         servo.mid()
         sleep(0.5)
         servo.max()
         sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")