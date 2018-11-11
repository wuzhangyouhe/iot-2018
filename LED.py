import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import sys

ledg = LED(16)
ledr = LED(20)
ledb = LED(21)

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# pin = 17 # pin 11 on the RP board
# GPIO.setup(pin, GPIO.OUT)
# state = int(sys.argv[1])
# GPIO.output(pin, (GPIO.LOW if state == 0 else GPIO.HIGH))

while True:
    ledg.on()
    ledr.on()
    ledb.on()
    sleep(1)
    ledg.off()
    ledr.off()
    ledb.off()
    sleep(1)

    
