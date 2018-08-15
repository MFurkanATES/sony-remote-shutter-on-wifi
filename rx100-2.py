#!/usr/bin/env python

"""RX100-2 interface shutter code for python"""

import json
import requests
import time


def take_picture():
    payload = get_payload("actTakePicture", [])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/camera', data=json.dumps(payload), headers=headers)
    j = json.loads(response)
    print j
    time.sleep(0.2)
    
def get_payload(method, params):
    return {
        "method": method,
        "params": params,
        "id": 1,
        "version": "1.0"
    }
while True:
  
    take_picture()
    #time.sleep(0.2) # istenilen zaman ayarlanabilir fakat gecikme var

