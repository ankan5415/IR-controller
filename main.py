from AWS_interfacing import PubSub
import os
import json
import ast
import serial
import time

#---init serial---
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

def send_signal():
    ser.write(b"1\n")

def convert_data(subtopic):
    payload = PubSub.get_payload(topic=os.getenv(subtopic))
    if payload:
        data = json.loads(payload.decode('utf-8'))
        body = ast.literal_eval(data["body"])
        desired_status = (body["desired_status"])
        return str(desired_status)


current_status = 0

if __name__ == "__main__":
    time.sleep(2)
    send_signal()
    while True:
        desired_status = convert_data("subtopic")
        if desired_status != current_status and desired_status != None: 
            print(desired_status)
            # print("message_sent")
            send_signal()
        
