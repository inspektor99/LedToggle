from twisted.web import server, resource
from twisted.internet import reactor
import RPi.GPIO as GPIO
import json
import pika

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)

LED1 = 11
LED2 = 15

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# Use plain credentials for authentication
mq_creds  = pika.PlainCredentials(
    username = "guest",
    password = "guest")

# Use localhost
mq_params = pika.ConnectionParameters(
    host         = "192.168.2.10",
    credentials  = mq_creds,
    virtual_host = "/")

# Anyone subscribing to topic "toggleled" receives our messages
mq_exchange    = "amq.topic"
mq_routing_key = "toggleled"

# This a connection object
mq_conn = pika.BlockingConnection(mq_params)

# This is one channel inside the connection
mq_chan = mq_conn.channel()

class HelloResource(resource.Resource):
    isLeaf = True
    toggleLed = "off"
    numberRequests = 0
    

    def render_GET(self, request):
        self.numberRequests += 1
        callback = request.args['callback'][0]

        if 'led' in request.args:
            self.toggleLed = request.args['led'][0]

        if self.toggleLed == "on":
            GPIO.output(LED1, True)
        else:
            GPIO.output(LED1, False)

        request.setHeader("content-type", "application/javascript")
        resp = {"data": "I am request #" + str(self.numberRequests), "led": self.toggleLed}

        resp = json.dumps(resp);
        mq_chan.basic_publish(exchange = mq_exchange, routing_key = mq_routing_key, body = resp)			
        return callback + "(" + resp + ");"

reactor.listenTCP(8080, server.Site(HelloResource()))
reactor.run()

