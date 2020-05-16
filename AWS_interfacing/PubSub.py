from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json
import os

AllowedActions = ['both', 'publish', 'subscribe']


payload = ""

def customCallback(client, userdata, message):
    global payload
    # print(message.payload)
    payload = message.payload


def get_payload(topic):
    global payload
    listen_on_subscription(topic)
    temp = payload
    if payload != "":
        payload = ""
        return temp


def listen_on_subscription(topic):
    
    if mode == 'both' or mode == 'subscribe':
        myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
    time.sleep(1)



def publish_to_topic():
    loopCount = 0
    while True:
        if mode == 'both' or mode == 'publish':
            message = {}
            message['message'] = "testerino"
            message['sequence'] = loopCount
            messageJson = json.dumps(message)
            myAWSIoTMQTTClient.publish(topic, messageJson, 1)
            if mode == 'publish':
                print('Published topic %s: %s\n' % (topic, messageJson))
            loopCount += 1
        time.sleep(1)





host = os.getenv("host")
rootCAPath = os.getenv("rootCAPath")
certificatePath = os.getenv("certificatePath")
privateKeyPath = os.getenv("privateKeyPath")
port = int(os.getenv("port"))
clientId = os.getenv("clientId")
topic = os.getenv("pubtopic")
mode = "both"



# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myAWSIoTMQTTClient.connect()



