"""
"""

import json
import requests


class Wrapper(object):
    """
    """
    def __init__(self, server, version, access_token):
        self.__server = server
        self.__version = version
        self.__access_token = access_token

    def api_call(self, method):
        endpoint = self.__server + self.__version
        headers = {"Authorization":"Bearer {}".format(self.__access_token)}
        url = endpoint + method
        return requests.get(url, headers=headers).json()
