"""
"""
from wrapper import Wrapper

if __name__ == '__main__':
    from credentials import *

    # http://developers.strava.com/docs/reference/
    server = "https://www.strava.com/"
    version = "api/v3/"
    wrapper = Wrapper(server, version, access_token)

    RESPONSE = wrapper.api_call("athlete")
    print("Athlete: {} {} - Id: {}".format(
        RESPONSE['firstname'],
        RESPONSE['lastname'],
        RESPONSE['id']))
