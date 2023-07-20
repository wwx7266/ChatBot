import yaml
import requests
import os



def get_access_token():
    dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(dir, "config.yaml")
    with open(config_file) as f:
        info = yaml.safe_load(f)

    api_key = info['api_key']
    secret_key = info['secret_key']

    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}' \
        .format(api_key, secret_key)

    response = requests.get(url)

    access_token = response.json()['access_token']

    return access_token
