class Sensor:

    def __init__(self,payload):
        self.name=payload['Client Name'].encode('ascii','replace')
        payload.pop('Client Name')
        self.time=payload['timestamp'].encode('ascii','replace')
        payload.pop('timestamp')
        self.readings=payload.copy()
