from AWS_interfacing import PubSub
import os
import json


while True:
    payload = PubSub.get_payload(topic=os.getenv("pubtopic"))
    if payload:
        data = json.loads(payload.decode('utf-8'))
        print(data)