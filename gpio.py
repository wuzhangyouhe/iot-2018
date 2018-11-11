import RPi.GPIO as GPIO
import sys
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 22 
GPIO.setup(pin, GPIO.OUT)
state = sys.argv[1]
GPIO.output(pin, (GPIO.LOW if state == 0 else GPIO.HIGH))
