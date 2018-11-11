#!/usr/bin/python
# coding=utf-8
 
# Needed modules will be imported
import RPi.GPIO as GPIO
#from gpiozero import LED
import Adafruit_DHT
import time
import paho.mqtt.client as mqtt
import time
import json
#from datetime import date, datetime
import datetime
import psutil
import os
import LCD2
import LED
#name of sensor client
client_name="Temperature_Humidity_sensor"

# The break of 2 seconds will be configured here
sleeptime = 2
 
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
 
# The pin which is connected with the sensor will be declared here
GPIO_Pin = 24

#mqtt server
#broker_address="alkaliexce.synology.me"
broker_address="220.255.109.155"

while True:
    try:
        LED.ledb.off()
        LED.ledr.off()
        LED.ledg.off()
        LED.ledg.on()
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
        now = datetime.datetime.now()
        now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        currentTime = now_str[10:]
        payload = '{ "Client Name" : "' + client_name + '", "timestamp" : "' + now_str + '","temperature" : ' + str(float(temper)) + ', "humidity" : ' + str(float(humid)) + ' }'
        LCD2.lcd_init()
        LCD2.lcd_string("Temperature %s%%"%temper,LCD2.LCD_LINE_1)
        LCD2.lcd_string("Humidity    %s"%humid,LCD2.LCD_LINE_2)
        LCD2.lcd_string("Date  %s%%"%now,LCD2.LCD_LINE_3)
        LCD2.lcd_string("Time  %s%%"%currentTime,LCD2.LCD_LINE_4)
        client = mqtt.Client("external_sensor")
        client.connect(broker_address, 1883, 60)
        #client.connect('192.168.1.100', 1883, 60)
        message = payload
        client.publish("mosquitto_sub/external", message)
        LED.ledg.off()
        client.disconnect()
        LED.ledb.on()
    #except (IOError, TypeError) as e:
    except Exception as e:    
        print(str(e))
        LED.ledg.off()
        LED.ledb.off()
        LED.ledr.on()# then reset the LCD's text
        #setText("")
    #finally:
    #    LCD2.lcd_clear()
    # wait some time before re-updating the LCD
    time.sleep(2)   
