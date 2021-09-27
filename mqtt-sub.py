import paho.mqtt.client as mqtt

cliente = mqtt.Client(client_id='devpy')
cliente.subscribe('casa/sala/lampada/2')

cliente.connect('localhost', port=1883)