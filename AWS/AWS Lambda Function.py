#desired status -> timestamp, desired status
import datetime
import json
import boto3

client = boto3.client('iot-data')



def lambda_handler(event, context):

    desired_status = event['queryStringParameters']["desired"]

    print(desired_status)

    ir_state = {}
    ir_state["timestamp"] = str(datetime.datetime.now())
    ir_state["desired_status"] = desired_status
    ir_state["message"] = "Received API Call"
    
    print(ir_state)

    return_message = {}
    return_message["statusCode"] = 200
    return_message['headers'] = {}
    return_message['headers']['Content-Type'] = 'application/json'
    return_message['body'] = json.dumps(ir_state)
    response = client.publish(
    topic='recv-data',
    qos=0,
    payload=json.dumps(return_message)
    )

    return return_message