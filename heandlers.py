from utils import *

def client_keyboard(inline: bool=False, achat: str='клиентский'):
    if achat == 'клиентский':
        keyboard = get_keyboard(
            [
                [('Расписание занятий', 'зелёный'), ('Расписание звонков', 'зелёный'), ],
                [('Расписание сессий', 'синий'), ('Чаты', 'синий')],
                [('Предложить идею', 'зелёный')],
                [('Связь и информация', 'красный')],
            ],
            inline=inline,
        )
        return keyboard

    if achat != 'клиентский':
        keyboard_chat = get_keyboard(
            [
                [('Добавление чатов', 'красный')],

            ],
            inline=inline,
        )

        return keyboard_chat

def client_command():
    message, chat_id, user_id = inic_msg()
    if message == 'начать':
        print(f'Запуск бота в беседе {chat_id}\n{message}')
    
    # if message == '!bd_list_01':
    #     sender(chat_id, text=f'Обновление базы в типе "Расписание занятий" от чата {chat_id}.\nОтправьте фото.')

    elif message == '!расписание':
        sender(chat_id, text='Отправьте ссылку на изображение.')
        message, chat_id, user_id = inic_msg()
        if VkEventType.MESSAGE_NEW and chat_id == 1:
            global new_mes
            new_mes = message
            sender(chat_id, text=f'Новое изображение добавлено',keyboard=client_keyboard())

    elif message == BOT_NAME+'расписание занятий':
        try:
            sender(chat_id, attachment=f'{new_mes}', keyboard=client_keyboard())
        except:
            sender(chat_id, attachment=f'photo-212220886_457239034', keyboard=client_keyboard())

    elif message == BOT_NAME+'расписание сессий':
        sender(chat_id, text='Сессии 3 семестра\n\nЭКЗАМЕН:\n'
        '✅Технология разработки программного обеспечения\n'
        '✅Инструментальные средства разработки программного обеспечения\n'
        '✅Математическое моделирование\n'
        '✅Осуществление интеграции программных модулей\n\nДИФФЕРЕНЦИРОВАННЫЙ ЗАЧЁТ:\n'
        '✅Практика по профилю специальности Осуществление интеграции программных модулей\n'
        '✅Учебная практика Осуществление интеграции программных модулей', keyboard=client_keyboard())
    
    elif message == BOT_NAME+'расписание звонков':
        sender(chat_id, attachment='photo-212220886_457239024', keyboard=client_keyboard())

    elif message == BOT_NAME+'связь и информация':
        sender(chat_id, text='236016, г. Калининград, ул. Артиллерийская, 18\n\nТелефон:\n+7 (4012) 97-10-68 - приемная директора колледжа\n+7 (4012) 97-12-31 - директор колледжа\n\nE-mail:\nspo-zf@ranepa.ru - приемная директора колледжа\n\nТелефонный справочник: https://goo-gl.me/RTEtY', keyboard=client_keyboard())

    elif message == BOT_NAME+'чаты':
        sender(chat_id, text='На данный момент в разработке.', keyboard=client_keyboard(True, 'team'))

    elif message == BOT_NAME+'предложить идею':
        sender(chat_id, text='Напишите свою идею сюда.')
        message, chat_id, user_id = inic_msg(True)
        if VkEventType.MESSAGE_NEW:
            sender(chat_id, text=f'Ваша идея "{message}" была отправлена разработчикам.\n[id{user_id}|{users_get(user_id)}]', keyboard=client_keyboard())