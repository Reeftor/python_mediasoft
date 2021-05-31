from urllib.parse import urljoin
from api_key import TOKEN
from random import randint

import requests
import json

HOST = 'https://api.telegram.org'
URI = '/bot{token}/{method}'


def get_me():
    method_name = 'getMe'

    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))

    response = requests.get(url)
    return response.json()


def get_updates(update_id=None):
    method_name = 'getUpdates'

    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))

    if not update_id:
        response = requests.get(url, params={'timeout': 10}, timeout=10)
    else:
        response = requests.get(url, params={'offset': update_id, 'timeout': 10}, timeout=10)
    return response.json()


def send_message(text, chat_id):
    method_name = 'sendMessage'

    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))

    reply_markup = {'keyboard': [[{'text': 'Flip a coin'}]]}
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}

    requests.post(url, data=data)


def flip_coin():
    num = randint(1, 100)
    return {
        num < 50: 'Heads',
        num == 50: 'Edge',
        num > 50: 'Tails'
    }[True]
