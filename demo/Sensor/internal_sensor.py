#!/usr/bin/python
# coding=utf-8
 
# Needed modules will be imported
import time
import paho.mqtt.client as mqtt
import logging
import time
import json
#from datetime import date, datetime
import datetime
import psutil
import os

#name of sensor client
client_name="internal_sensor_1"

# The break of 2 seconds will be configured here
sleeptime = 2

#mqtt server
#broker_address="alkaliexce.synology.me"
broker_address="192.168.1.103"
def on_log(client, userdata, level, buf):
    print("log: ",buf)

while True:
    try:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        cpuTemp = psutil.cpu_times(percpu=True)[0].user
        now = datetime.datetime.now()
        now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        currentTime = now_str[10:]
        payload = '{ "Client Name" : "' + client_name + '", "timestamp" : "' + now_str +'", "CPU utilization" : ' + str(float(cpu)) + ', "Memory utilization" : ' + str(float(mem)) + ', "CPU Temperature" : ' + str(float(cpuTemp)) + ' }'

        client = mqtt.Client("internal_sensor")
        #client.on_log=on_log
        client.connect(broker_address,1883,60)
        message = payload
        client.publish("mosquitto_sub/internal", message)
        client.disconnect()
        #print(message)
        time.sleep(0.5)
    except (IOError, TypeError) as e:
        print(str(e))
    time.sleep(sleeptime)
