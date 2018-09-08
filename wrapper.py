"""
"""

import json
import requests

from credentials import *
payload = {'AccessToken': access_token}

ENDPOINT = "https://www.strava.com/"
VERSION = "api/v3/"

URL = ENDPOINT + VERSION
headers = {"Authorization":"Bearer {}".format(access_token)}
endpoint = URL + "athlete"
response = requests.get(endpoint,headers=headers)

print(response.json())
