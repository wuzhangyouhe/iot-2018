from BaseHTTPServer import BaseHTTPRequestHandler
from sensor import Sensor
import json
import paho.mqtt.client as mqtt
import threading

broker_address="alkaliexce.synology.me"

sensors=dict()

def html_response():
	html='<h1 style="text-align:center;">Sensors Monitoring System</h1>'
	for sensor_name,sensor_object in sensors.iteritems():
		header=""
		values=""

		for key,value in sensor_object.readings.iteritems():
			header=header+"<th>"+key.encode('ascii','replace')+"</th>"
			values=values+"<td>"+str(value)+"</td>"
		body="""<div style="text-align:center;">
		<h3>%s</h3>
		<h4>Last Updated: %s</h4>
		<table border=1 style="margin: 0 auto;">
		<tr>
		%s
		</tr>
		<tr>
		%s
		</tr>
		</table>
		</div>
		"""%(sensor_object.name,sensor_object.time,header,values)
		html = html + body

	return html

def on_message(mqttc, userdata, mesg):
	payload = json.loads(mesg.payload)
	print(sensors)
	if('Client Name' not in payload or 'timestamp' not in payload):
		print(payload)
		print('Invalid data')
		return
	sensor=Sensor(payload)
	sensor.name
	sensors.update({sensor.name:sensor})

def mqtt_thread():
	client = mqtt.Client("http_server")
	client.connect(broker_address, 1883, 60)
	client.on_message = on_message
	client.subscribe("mosquitto_sub/#")
	client.loop_forever()

class GetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        message = html_response()
        self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        self.do_GET()


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    t1 = threading.Thread(target=mqtt_thread)
    t1.start()
    server.serve_forever()


