import stravalib
from tri.handlers.static import strava_configs
import requests

class StravaHandler(object):

    def __init__(self, app_key):
        _config = getattr(strava_configs, app_key)
        _client = stravalib.client.Client()
        authorize_url = _client.authorization_url(_config['client_id'], redirect_uri='http://127.0.0.1:5000/authorization')
        res = requests.get(authorize_url)

        _client.access_token = _config['token']
        self.client = _client