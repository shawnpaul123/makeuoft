import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Motor channels
motor_channel = (5, 6, 13, 19)
GPIO.setup(motor_channel, GPIO.OUT)

def motor_spin(duration, direction=True, dt=0.00):
	# Min dt is 0.002 s
	start = time.time()
	if direction:
		while time.time() < start + duration:
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(dt)
	else:
		while time.time() < start + duration:
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.LOW,GPIOGPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(0.02)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(0.02).HIGH,GPIO.HIGH,GPIO.LOW))
			sleep(dt)
			GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
			sleep(dt)
	return

motor_spin(1)