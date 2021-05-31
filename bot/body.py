from functions import *
from requests.exceptions import ReadTimeout


def get_message_params():
    next_update_id = None
    while True:
        try:
            res = get_updates(next_update_id)
        except ReadTimeout:
            continue

        for update in res.get('result', []):
            if 'message' in update:
                yield [update['message'].get('text'),
                       update['message'].get('chat').get('id'),
                       update['message'].get('chat').get('first_name')]
            else:
                ...

        next_update_id = res['result'][-1].get('update_id') + 1


def cycle():
    bot_name = get_me().get('result').get('first_name')

    for text, chat_id, user_name in get_message_params():
        welcome_message = f'Hello {user_name}, my name is {bot_name}! :) \nPress the button "Flip a coin"' \
                          f' and i will tell you which side the coin fell on.\nHeads or tails.\nGood Luck!'
        if text == '/start':
            send_message(welcome_message, chat_id)
        elif text == 'Flip a coin':
            result = flip_coin()
            if result == 'Heads':
                send_message('It\'s Heads!', chat_id)
            elif result == 'Tails':
                send_message('It\'s Tails!', chat_id)
            else:
                send_message('Oh my God, It\'s Edge!!!', chat_id)
