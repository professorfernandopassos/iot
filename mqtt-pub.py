import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

client = mqtt.Client('pubpy')
client.connect(BROKER, PORT)

def on_publish_callback(client, userdata, result):
    print("Dado publicado")

client.on_publish = on_publish_callback

while(True):
    value = input('Digite 1 para ligado ou 0 para desligado: ')
    status = "false"
    if(value == "0"):
        status = "false"
    elif(value == "1"):
        status = "true"
    client.publish('casa/sala/lampada/1','{ "status": %s }' % str(status))
    print('{ "status": %s }' % str(status))
    # value = input('Digite 1 para ligado ou 0 para desligado: ')
    # status = False
    # if(value == "0"):
    #     status = False
    # elif(value == "1"):
    #     status = True
    # client.publish('casa/sala/lampada/1','{ "status": %s }' % str(status).lower())
    # print('{ "status": %s }' % str(status).lower())
    



