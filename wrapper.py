"""
"""

import json
import requests

from credentials import *

# http://developers.strava.com/docs/reference/
SERVER = "https://www.strava.com/"
VERSION = "api/v3/"

ENDPOINT = SERVER + VERSION
HEADERS = {"Authorization":"Bearer {}".format(access_token)}
URL = ENDPOINT + "athlete"
RESPONSE = requests.get(URL, headers=HEADERS).json()

print("Athlete: {} {} - Id: {}".format(
    RESPONSE['firstname'],
    RESPONSE['lastname'],
    RESPONSE['id']))
