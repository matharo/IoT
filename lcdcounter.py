import RPi.GPIO as GPIO
from import time *
import I2C_LCD_driver
import smbus

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin, 3V

lcd = I2C_LCD_driver.lcd()

while True:
sensor=GPIO.input(11)
if sensor==0:                 	#When output from motion sensor
	GPIO.output(3, 0)  			#Turn off LED
elif sensor==1:
	GPIO.output(3, 1)  			#Turn on LED
	
	i = 30
	while i != 0:
		lcd.lcd_display_string(i,1)
		time.sleep(1)
		i--
	GPIO.output(3,0)				#turn off sensor after 30 seconds