"""
"""

import json
import requests

from credentials import *

SERVER = "https://www.strava.com/"
VERSION = "api/v3/"

ENDPOINT = SERVER + VERSION
HEADERS = {"Authorization":"Bearer {}".format(access_token)}
URL = ENDPOINT + "athlete"
RESPONSE = requests.get(URL, headers=HEADERS)

print(RESPONSE.json())
