#!/usr/bin/python
# coding=utf-8
 
# Needed modules will be imported
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from mosquitto import *
import logging
import time
import json
#from datetime import date, datetime
import datetime
import psutil
import os
import LCD2

# The break of 2 seconds will be configured here
sleeptime = 2
 
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
 
# The pin which is connected with the sensor will be declared here
GPIO_Pin = 24
 
print('KY-015 sensortest - temperature and humidity')

while True:
    try:
        #cpu = psutil.cpu_percent()
        #mem = psutil.virtual_memory().percent
        #cpuTemp = psutil.cpu_times(percpu=True)[0].user
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
        now = datetime.datetime.now()
        now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        currentTime = now_str[10:]
        payload = '{ "timestamp" : "' + now_str + '","temperature" : ' + str(float(temper)) + ', "humidity" : ' + str(float(humid)) + ' }'
        #payload = '{ "timestamp" : "' + now_str + '", "CPU utilization" : ' + str(float(cpu)) + ', "Memory utilization" : ' + str(float(mem)) + ', "CPU Temperature" : ' + str(float(cpuTemp)) + ' }'
	#payload = json.dumps(data)
	#print (payload)
        LCD2.lcd_init()
        LCD2.lcd_string("Temperature %s%%"%temper,LCD2.LCD_LINE_1)
        LCD2.lcd_string("Humidity    %s"%humid,LCD2.LCD_LINE_2)
        LCD2.lcd_string("Date  %s%%"%now,LCD2.LCD_LINE_3)
        LCD2.lcd_string("Time  %s%%"%currentTime,LCD2.LCD_LINE_4)
	client = Mosquitto("my_id_pub")
        #client.connect("alkaliexce.synology.me")
        client.connect("220.255.109.155")
        #client.connect("localhost")
        message = payload
        topic = "temp"
        client.publish(topic, message)
        client.disconnect()
        time.sleep(0.5)
    except (IOError, TypeError) as e:
        print(str(e))
        # then reset the LCD's text
        #setText("")
    #finally:
    #    LCD2.lcd_clear()
    # wait some time before re-updating the LCD
    time.sleep(2)   
