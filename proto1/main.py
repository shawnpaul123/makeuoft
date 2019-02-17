import RPi.GPIO as GPIO
from time import sleep, time

# Setup GPIO interface
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set GPIO motor pins
motor_channel_A = [29, 31, 33, 35]
motor_channel_B = [32, 36, 38, 40]

# Set GPIO button pins
btn_A = 8
btn_B = 10

# Setup motor arrays and I/O
motors = [motor_channel_A, motor_channel_B]
GPIO.setup(motors[0], GPIO.OUT)
GPIO.setup(motors[1], GPIO.OUT)

# Setup button I/O
btns = [btn_A, btn_B]
GPIO.setup(btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Clockwise solenoid energization sequence
seq_cw = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]

# Counterclockwise solenoid energization sequence
seq_ccw = seq_cw[::-1]

GPIO.add_event_detect(btn_A, GPIO.RISING, \
	bouncetime=200)
GPIO.add_event_detect(btn_B, GPIO.RISING, \
	bouncetime=200)

# Motor functions
def stop_motors(pin=-1):
	if pin == btn_A:
		GPIO.output(motors[0], 0)
		print("motor A stop")
	elif pin == btn_B:
		GPIO.output(motors[1], 0)
		print("motor B stop")
	else:
		GPIO.output(motors[0], 0)
		GPIO.output(motors[1], 0)

def move_A(duration, dir=True, dt=0.002):
	# Duration in seconds
	# dir = True => CW
	# dt is motor step time
	start = time()
	stop = False
	if dir == 1:
		seq = seq_cw
	elif dir == -1:
		seq = seq_ccw
	else:
		return
	while time() < start + duration and stop == False:
		for step in seq:
			GPIO.output(motors[0], step)
			sleep(dt)
			if GPIO.event_detected(btn_A):
				print("Motor A stop")
				stop = True
				break
				
	# Motors off
	stop_motors()

def move_B(duration, dir=True, dt=0.002):
	# Duration in seconds
	# Dir = True => CW
	# dt is motor step time
	start = time()
	stop = False
	if dir == 1:
		seq = seq_cw
	elif dir == -1:
		seq = seq_ccw
	else:
		return
	while time() < start + duration and stop == False:
		for step in seq:
			GPIO.output(motors[1], step)
			sleep(dt)
			if GPIO.event_detected(btn_B):
				print("Motor B stop")
				stop = True
				break
	# Motors off
	stop_motors()

try:
	print("1: Motor A up")
	timeUp = 5
	move_A(timeUp)

	print("2: Motor B forward")
	move_B(20)

	print("3: Wait 5s")
	sleep(5)

	print("4: Motor B backward")
	move_B(20, -1)

	print("5: Motor A down")
	move_A(20, -1)

except KeyboardInterrupt:
	print("Keyboard interrupt.")

finally:
	# Stop all motors
	stop_motors()
	print("Motors off.")

	# Reset all GPIO pins
	GPIO.cleanup()
