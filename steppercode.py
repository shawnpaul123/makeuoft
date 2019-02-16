import RPi.GPIO as GPIO
from time import sleep
import sys

# Assign GPIO pins for stepper motor
motor_channel = (29, 31, 33, 35)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_channel, GPIO.OUT)

# True = Clockwise, False = Anticlockwise
motor_direction = True;

while True:
	try:
		if motor_direction:
			print("Motor running clockwise")
			GPIO.output(motor_channel, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(0.02)
		else:
			print("Motor running anticlockwise")
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(0.02)
	except KeyboardInterrupt:
		GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
		sys.exit(0)