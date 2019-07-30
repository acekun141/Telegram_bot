from flask import Flask
from flask import request
from flask import json
from flask import Response
from telegram_bot import telegram_bot
from check import Check
import json
import requests

with open('config.json') as config_file:
    data = json.load(config_file)

app = Flask(__name__)

def prase_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    return chat_id, txt


@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt = prase_message(msg)
        try:
            checking = Check(txt)
            if checking.msg_for_bot():
                bot.send_message(checking.msg_for_bot(),chat_id)
        except Exception as value:
            bot.send_message(str(value),chat_id)
        return Response('OK', status=200)
    else:
        return '<h1>Ngon</h1>'

if __name__ == "__main__":
    try:
        bot = telegram_bot(data['bot']['token'])
        app.run(debug=True)
    except Exception as value:
        print(value)