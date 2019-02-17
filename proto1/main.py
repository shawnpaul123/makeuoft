import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Motor channels
motor_channel = (29, 31, 33, 35)
GPIO.setup(motor_channel, GPIO.OUT)

def motor_spin(duration, direction=True, dt=0.002):
	# Min dt is 0.002 s
	start = time()
	if direction:
		while time() < start + duration:
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(dt)
	else:
		while time() < start + duration:
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(dt)
	return

try:
	motor_spin(100, False)
except KeyboardInterrupt:
	GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
	GPIO.cleanup()
	print("Motor off.")
