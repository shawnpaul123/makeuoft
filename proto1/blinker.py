import RPi.GPIO as GPIO
from time import sleep

def btn_callback(channel):
	print("Btn pushed")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

try:
	while True:
		GPIO.output(18, GPIO.HIGH)
		sleep(0.25)
		GPIO.output(18, GPIO.LOW)
		sleep(0.25)
except KeyboardInterrupt:
	print("Closing.")
	GPIO.cleanup()
