import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
green = 23
GPIO.setup(green, GPIO.OUT)

toggle = True
while True:
	GPIO.output(green, toggle)
	toggle = not toggle
	time.sleep(1)
