from mosquitto import *
import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication

def on_message(mqttc, userdata, mesg):
    #print "message: % %" %(str(mesg.topic), json.dumps(mesg.payload, indent=4))
    Topic = str(mesg.topic)
    #message = json.loads(json.dumps(mesg.payload, indent=4))
    message = json.dumps(mesg.payload, indent=4)
    print (Topic)
    print (message)
    humidity = float(message[-7:-3])
    if (humidity > 90):
	print (humidity)
	msg = MIMEMultipart()
	msg['Subject'] = "Test notification! Alter action"
	body = "Alert Notfication from IOT 2018 project. \n Dear, the outsource datacenter humidity is over 90%. It will be risk for the devices operation."
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("IW2018networking@gmail.com", "IW2018net")
	server.sendmail("IW2018networking@gmail.com", "e0146965@u.nus.edu", msg.as_string())
	print('e-mail sent!')
	server.quit()

client = Mosquitto("my_id_sub")
#client.connect("alkaliexce.synology.me")
client.connect("192.168.1.101")
client.on_message = on_message
client.subscribe("#")
while True:
    client.loop()
