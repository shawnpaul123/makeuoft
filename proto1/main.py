import RPi.GPIO as GPIO
from time import sleep, time

# Setup GPIO interface
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set GPIO motor pins
motor_channel_A = [29, 31, 33, 35]
motor_channel_B = [32, 36, 38, 40]

# Setup motor arrays
motors = [motor_channel_A, motor_channel_B]
GPIO.setup(motors[0], GPIO.OUT)
GPIO.setup(motors[1], GPIO.OUT)

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

try:
	while True:
		move_A(1, True)
		move_A(1, False)
		move_B(1, True)
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
