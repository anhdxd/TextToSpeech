#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import the json library
from cgi import test
import json
import requests
import urllib
import io
filename="C:/Users/Anhdz/Desktop/new 7.txt"

with io.open(filename,'r',encoding='utf8') as f:
    text = f.read()

url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"

data = {"text": "", "voice": "hn-quynhanh", "id": "2", "without_filter": True, "speed": 1, "tts_return_option": 2}
data["text"]=text
headers = {'Content-type': 'application/json', 'token': 'z19N2UJqu-BW5hWUoR2Nux6U8Xg6Mz5FGPZKuFTLbZC9CWp0VgxGfd4jEMiJ7cp1'}
response = requests.post(url, data=json.dumps(data), headers=headers)
#if encounter SSL error because of https certificate, please comment out above line and use the line below to  make insecure connections   (this will expose your application to security risks, such as man-in-the-middle attacks.)
#response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
# Headers is a dictionary
print(response.headers)
# Get status_code.
print(response.status_code)
# Get the response data as a python object.
data = response.content
f = open("tanpk.wav", "wb")
f.write(data)
f.close()