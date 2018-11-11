import RPi.GPIO as GPIO
import time
 
class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
 
    def getState(self):
        return GPIO.input(self.pin)
 
def main():
    sensor = Sensor(4)
    state = sensor.getState()
    while True:
        time.sleep(0.1)
        r = sensor.getState()
        if (r != state):
            state = r
            print "%s: status is %d" % (time.asctime(), state)
 
if __name__ == "__main__":
    main()
