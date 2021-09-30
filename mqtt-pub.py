import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

client = mqtt.Client('pubpy')
client.connect(BROKER, PORT)

