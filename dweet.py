import dweepy, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
green = 23
GPIO.setup(green, GPIO.OUT)

toggle = False
while True:
    latest = dweepy.get_latest_dweet_for('hilarious-structure')
    latest_x = latest[u'with'][0][u'content'][u'tilt_x']
    print latest_x
    toggle = (latest_x < 0)
    GPIO.output(green,toggle)

