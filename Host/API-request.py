import requests
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Send a value to an AWS API')
parser.add_argument("-s", "--state", action="store", required=True, dest="state", help="Desired state for heater")

args = parser.parse_args()
desired = args.state
print(desired)

r = requests.get(os.getenv("api-client"), params = {'desired':int(desired)})
print(r.json())
