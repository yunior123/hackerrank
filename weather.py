#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTemperature' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/weather?name=<name>
#
# The function is expected to return an Integer.
# The function accepts a singe parameter name.
# ex response
# {
#     "name": "San Francisco",
#     "weather": "12 degree",
# }

def getTemperature(name):
    # Write your code here
    import requests
    import json
    url = f"https://jsonmock.hackerrank.com/api/weather?name={name}"
    response = requests.get(url)
    data = response.json()
    return int(data['data'][0]['weather'].split()[0])

