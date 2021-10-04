import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

client = mqtt.Client('pub-py')
client.connect(BROKER, PORT)

def on_publish_callback(client, userdata, result):
    print("Dado publicado")

client.on_publish = on_publish_callback

status = "false"

while(True):
    value = input('Digite 1 para ligado ou 0 para desligado: ')
    
    if(value == "0"):
        status = "false"
    elif(value == "1"):
        status = "true"

    client.publish('casa/sala/lampada/1','{ "status": %s }' % status)
    print('{ "status": %s }' % status)
    # value = input('Digite 1 para ligado ou 0 para desligado: ')
    # status = False
    # if(value == "0"):
    #     status = False
    # elif(value == "1"):
    #     status = True
    # client.publish('casa/sala/lampada/1','{ "status": %s }' % str(status).lower())
    # print('{ "status": %s }' % str(status).lower())
    



