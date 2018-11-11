import paho.mqtt.client as mqtt
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication

broker_address="alkaliexce.synology.me"

def treshold_reached(temp,humidity):
	if humidity>90:
		return True


def on_message(mqttc, userdata, mesg):
	#print "message: % %" %(str(mesg.topic), json.dumps(mesg.payload, indent=4))
	# Topic = str(mesg.topic)
	#message = json.loads(json.dumps(mesg.payload, indent=4))
	payload = json.loads(mesg.payload)
	if('temperature' not in payload or 'humidity' not in payload):
		print(payload)
		print('Invalid data')
		return
	if (treshold_reached(payload['temperature'],payload['humidity'])):
		msg = MIMEMultipart()
		msg['Subject'] = "Test notification! Alter action"
		body = "Alert Notfication from IOT 2018 project. \n Dear, the environmental threshold has been reached. It will be risk for the devices operation."
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("IW2018networking@gmail.com", "IW2018net")
		server.sendmail("IW2018networking@gmail.com", "e0146965@u.nus.edu", msg.as_string())
		print('e-mail sent!')
		server.quit()

client = mqtt.Client("monitor_trigger")
client.connect(broker_address, 1883, 60)
client.on_message = on_message
client.subscribe("mosquitto_sub/#")
client.loop_forever()
