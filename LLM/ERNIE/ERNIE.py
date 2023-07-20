import requests
import json
from .utils import get_access_token
from ..ChatManager.chat_history import History

class ERNIE:

    def __init__(self):
        self.token = get_access_token()
        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={}" \
            .format(self.token)
        self.history = History()

    def chat(self, message, temperature=0.85):
        self.history.add_user_message(message)
        payload = json.dumps({
            "messages": self.history.get_chat_history(),
            "temperature": temperature,
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", self.url, headers=headers, data=payload)

        response_json = response.json()

        if 'error_code' in response_json.keys():
            print("error code: {}".format(response_json['error_code']))
            print("error msg: {}".format(response_json['error_msg']))

            return response_json['error_code']

        message_response = response_json['result']
        self.history.add_response_message(message_response)
        print("assistant: {}".format(message_response))
        return message_response

