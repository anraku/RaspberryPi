import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

count = 0
#GPIO.output(25, GPIO.HIGH)

while True:
	inputValue = GPIO.input(24)
	if(inputValue == True):
		count = count + 1
		print("Button pressed" + str(count) + " times.")
	time.sleep(.01)

