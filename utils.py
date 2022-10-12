from tracemalloc import DomainFilter
import vk_api
import json
from config import *
from vk_api.longpoll import VkLongPoll, VkEventType

def inic_client():
    global vk_session
    global longpoll
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk_session)

def inic_msg(ilon: bool=False):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_chat:
            if ilon == False:
                message = event.text.lower()
            else:
                message = event.text
            chat_id = event.chat_id
            user_id = event.user_id
            return message, chat_id, user_id

def sender(chat_id: int, user_id: int=None, domain: str=None, text: str=None, attachment: str=None, keyboard=None, template=None, intent: str=None, ):
    vk_session.method('messages.send', {
                        'user_id': user_id,
                        'domain': domain,
                        'chat_id': chat_id,
                        'message': text,
                        'random_id': 0,
                        'attachment': attachment,
                        'keyboard': keyboard,
                        'template': template,
                        'intent': intent,
                        }
                    )

def users_get(user_ids: str):
    users_get = vk_session.method('users.get', {
                        'user_ids': user_ids,
                        }
                    )
    user_name = users_get[0]['first_name'] + ' ' + users_get[0]['last_name']
    return user_name

def get_keyboard(buts, inline: bool=False):
    global get_but
    nb = []
    color = ''
    for i in range(len(buts)):
        nb.append([])
        for j in range(len(buts[i])):
            nb[i].append(None)
    for i in range(len(buts)):
        for j in range(len(buts[i])):
            text = buts[i][j][0]

            if buts[i][j][1] == 'с' or buts[i][j][1] == 'синий' or buts[i][j][1] == 'p' or buts[i][j][1] == 'primary':
                # Синий
                color = 'primary'
            elif buts[i][j][1] == 'б' or buts[i][j][1] == 'белый' or buts[i][j][1] == 's' or buts[i][j][1] == 'secondary':
                # Белый
                color = 'secondary'
            elif buts[i][j][1] == 'з' or buts[i][j][1] == 'зелёный' or buts[i][j][1] == 'ps' or buts[i][j][1] == 'positive':
                # Зелёный
                color = 'positive'
            elif buts[i][j][1] == 'к' or buts[i][j][1] == 'красный' or buts[i][j][1] == 'n' or buts[i][j][1] == 'negative':
                # Красный
                color = 'negative'
            nb[i][j] = {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }
    first_keyboard = {
        'one_time': False,
        'buttons': nb,
        'inline': inline,
    }
    first_keyboard = json.dumps(
    first_keyboard, ensure_ascii=False).encode('utf-8')
    first_keyboard = str(first_keyboard.decode('utf-8'))
    return first_keyboard

def commands(func):
    def wrapper(lists: list | None):
        if lists != '':
            func()
        else:
            return False