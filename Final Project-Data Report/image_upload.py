#!/usr/bin/env python3 

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
directory = '/home/student/supplier-data/images'

for filename in os.listdir(directory):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"): 
        with open(os.path.join(directory, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})