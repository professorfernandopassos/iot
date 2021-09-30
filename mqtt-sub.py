import paho.mqtt.client as mqtt
import time

client = mqtt.Client(client_id='devpy')

client.connect('localhost', port=1883)
client.subscribe('casa/sala/lampada/1')

print("Subscriber connected")

def on_message_callback(client, userdata, message):
    print(message.payload.decode('utf-8'))

client.on_message = on_message_callback

client.loop_forever()
# time.sleep(100)
# client.loop_stop()