import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Speed of sound
c = 343			# [m/s]

# Set pins
GPIO_TRIGGER = 14
GPIO_ECHO = 12

# Set GPIO direction
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
	# Fire ultrasound pulse, set trigger to high
	GPIO.output(GPIO_TRIGGER, True)

	# Deactivate pulse, set trigger to low
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# Wait for pulse to return
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	# Save arrival time
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime

	distance = TimeElapsed * c / 2;
	return distance

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print("Distance = %.1f m" % dist)
			time.sleep(1)
	except KeyboardInterrupt:
		print("Measurement stopped.")
		GPIO.cleanup()