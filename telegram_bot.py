import time
import json
import requests

class telegram_bot:
    def __init__(self,token):
        self.token = token
    def send_message(self,msg,id):
        url = 'https://api.telegram.org/bot' + self.token + '/sendMessage'
        payload = {'chat_id':id, 'text':msg}
        r = requests.post(url, json=payload)
        return r
