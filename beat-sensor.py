#!/usr/bin/python
# coding=utf-8
 
#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
###
### Parts of Code based on Dan Truong's KY039 Arduino Heartrate Monitor V1.0
### [https://forum.arduino.cc/index.php?topic=209140.msg2168654] Message #29
#############################################################################################################
 
 
# This code is using the ADS1115 and the I2C python libraries for the Raspberry Pi
# It is published by BSD License under the following link
# [https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code]
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
 
# Additional needed modules will be imported and configured
import time, signal, sys, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Used variables will be initialized
beatsPerMinute = 0
isPeak = False
result = False
delayTime = 0.01
maxValue = 0
schwelle = 25
beatTime = 0
oldBeatTime = 0
 
# Address allocation ADS1x15 ADC
 
ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit
 
# Amplification (Gain) will be picked 
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V
 
# Sample rate of the ADC (SampleRate) will be picked 
sps = 8    # 8 Samples per second
# sps = 16   # 16 Samples per second
# sps = 32   # 32 Samples per second
# sps = 64   # 64 Samples per second
# sps = 128  # 128 Samples per second
# sps = 250  # 250 Samples per second
# sps = 475  # 475 Samples per second
# sps = 860  # 860 Samples per second
 
# ADC-Channel (1-4) will be picked 
adc_channel = 0    # Channel 0
# adc_channel = 1    # Channel 1
# adc_channel = 2    # Channel 2
# adc_channel = 3    # Channel 3
 
# Here, the ADC will be initialized - the ADC which is used by the KY-053 is an ADS1115 chipset
adc = ADS1x15(ic=ADS1115)
 
# LED output pin declaration.
LED_PIN = 7
GPIO.setup(LED_PIN, GPIO.OUT, initial= GPIO.LOW)
 
 
#############################################################################################################
 
# Buzzer output pin declaration.
def heartBeatDetect(schwelle):
        global maxValue
        global isPeak
        global result
        global oldBeatTime
 
        # Reading of the voltage at the photo transistor
        # saving of the voltage value into the rawValue variable
        # With "adc_channel" the channel which is connected with the ADC will be picked.
        rawValue = adc.readADCSingleEnded(adc_channel, gain, sps)
 
        # Reset of the result-variable 
        if result == True:
            result = False
 
        # If the difference between the current value and the last maximum value is to big
        # (maybe bacause you moved the finger to strong for example)
        # Here you see the reset of the maxValue to get a new basic.
        if rawValue * 4 < maxValue:              maxValue = rawValue * 0.8;                # Detecting of the peak. If a new raWValue is higher than the last maxValue,        # it will be detected as a peak from the data.        if rawValue > (maxValue - schwelle):
 
              if rawValue > maxValue:
                    maxValue = rawValue
              # One heartbeat will assign to the peak
              if isPeak == False:
                    result = True
 
              isPeak = True
 
        else:
            if rawValue < maxValue - schwelle:
              isPeak = False
              # Here the max value will be decreased at each run
              # because if you don't do that the value would be every time lower or the same.
              # Also if you move the finger a bit the signal would be weaker without that.
 
            maxValue = maxValue - schwelle/2
 
        # If a heartbeat was detected above, the Output will start.
        if result == True:
 
            # Calculating of the pulse
            # Here the system time will be recorded for every heartbeat
            # At the next heartbeat, the system time will be compared with the last recorded one
            # The difference between them is the time between the heartbeats
            # with that you can also calculate the pulse
            beatTime = time.time()
            timedifference = beatTime - oldBeatTime
            beatsPerMinute = 60/timedifference
            oldBeatTime = beatTime
 
            # Additional to the caltulating of the pulse, the heartbeat will light up a LED for a short time
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(delayTime*10)
            GPIO.output(LED_PIN, GPIO.LOW)
 
            # Calculated pulse will be given to the function
            return beatsPerMinute
 
#############################################################################################################
 
# ########
# Main program loop
# ########
# After the "delayTime" (standard: 10ms) the function to detect a heartbeat will start.
# After detecting a heartbeat, the pulse will be outputted.
 
try:
        while True:
                time.sleep(delayTime)
                beatsPerMinute = heartBeatDetect(schwelle)
                if result == True:
                    print "---Heartbeat detected !--- Puls:", int(beatsPerMinute),"(bpm)"
 
 
 
except KeyboardInterrupt:
        GPIO.cleanup()
