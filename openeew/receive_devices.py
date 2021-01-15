import json

import paho.mqtt.client as mqtt

from devices import save_device
from mqtt import authenticate
from os import getenv

mqtt_username = getenv('username','')
mqtt_password = getenv('password','')
mqtt_port = getenv('MOSQUITTO_SERVICE_PORT_MQTT', 1883)

def on_connect(client, userdata, flags, resultCode):
    print(f'✅ Connected with result code {resultCode}')
    client.subscribe('/devices')


def on_message(client, userdata, message):
    try:
        decoded_message = str(message.payload.decode('utf-8', 'ignore'))
        device = json.loads(decoded_message)
        print(f'Received device: {device}')
        save_device(device)
        print('✅ Device saved')
    except BaseException as exception:
        print(exception)


client = authenticate(mqtt.Client())
client.enable_logger()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.connect('localhost', int(mqtt_port))

print('👂🚀 Listening for devices')
client.loop_forever()
