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

# Motor functions
def move_A(duration, dir=True, dt=0.002):
	# Duration in seconds
	# dir = True => CW
	# dt is motor step time
	start = time()
	if dir:
		seq = seq_cw
	else:
		seq = seq_ccw
	while time() < start + duration:
		for step in seq:
				GPIO.output(motors[0], step)
				sleep(dt)
	# Motors off
	GPIO.output(motors[0], 0)

def move_B(duration, dir=True, dt=0.002):
	# Duration in seconds
	# dt is motor step time
	start = time()
	if dir:
		seq = seq_cw
	else:
		seq = seq_ccw
	while time() < start + duration:
		for step in seq:
				GPIO.output(motors[1], step)
				sleep(dt)
	# Motors off
	GPIO.output(motors[1], 0)
	
#Shawn's stuff	
def click_button(button_type):
	# waiting for button press
	while True:
		try:
		input_state = GPIO.input(btn_B)
			if input_state = True:
				print('Buttton Pressed to Stop Motors')
				# Stop all motors
				GPIO.output(motors[0], 0)
				GPIO.output(motors[1], 0)
				print("Motors off.")
				break

	except KeyboardInterrupt:
		print("Keyboard interrupt.")
		
		

try:
	move_A(1, True)
	move_B(1, True)

	# Wait for buttonpress
	while True:
		input_state = GPIO.input(btn_A)
		n = 0
		if input_state == True:
			print('Button Pressed')
			n += 1
			sleep(0.2)
		if n >= 10:
			break

	move_A(1, False)
	move_B(1, False)
except KeyboardInterrupt:
	print("Keyboard interrupt.")
finally:
	# Stop all motors
	GPIO.output(motors[0], 0)
	GPIO.output(motors[1], 0)
	print("Motors off.")

	# Reset all GPIO pins
	GPIO.cleanup()
	
	
	
