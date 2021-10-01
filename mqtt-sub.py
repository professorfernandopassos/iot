import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client(client_id='devpy')

client.connect('localhost', port=1883)
client.subscribe('casa/sala/lampada/1')
# client.subscribe('casa/sala/lampada/1/intensidade')

print("Subscriber connected!")

def on_message_callback(client, userdata, message):
    # print(message.payload.decode('utf-8'))
    msg = json.loads(message.payload.decode('utf-8'))
    if(msg["status"] == True):
        # Liga pino do raspberry / arduino
        print("Pino X ligado")
    elif(msg["status"] == False):
        # Desliga pino do raspberry / arduino
        print("Pino X desligado")

    # if(msg["value"]):
        # Lampada na intensidade x




    # print(message.payload.decode('utf-8'))

client.on_message = on_message_callback

client.loop_forever()
# client.loop_start()
# time.sleep(100)
# client.loop_stop()

