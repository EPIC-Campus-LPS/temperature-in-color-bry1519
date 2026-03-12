import time
import board
import adafruit_dht
from datetime import datetime
import RPi.GPIO as GPIO

LED_BLUE = 25
LED_RED = 18
TEMP_PIN = board.D16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)


sensor = adafruit_dht.DHT11(board.D16)

def turn_off_LEDS():
	GPIO.output(LED_BLUE, GPIO.LOW)
	GPIO.output(LED_RED, GPIO.LOW)

def to_fahrenheit(c):
	f = (c*9/5)+32
	return f


print ("time,celsius,fahrenheit")

while True:
	try:
		celsius = sensor.temperature
		fahrenheit = to_fahrenheit(celsius)
		current_time = datetime.now()
		print ("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
		time.sleep(3.0)

		turn_off_LEDS()

		if fahrenheit < 72:
			GPIO.output(LED_BLUE, GPIO.HIGH)
			print ("status: cold(LED_BLUE)")
		else:
			GPIO.output(LED_RED, GPIO.HIGH)
			print ("status: HOT(LED_RED)")
		time.sleep(3.0)
		
		print ("\Stopped program")
		
	except Exception as error:
		turn_off_LEDS()
		sensor.exit()
		raise error
