import telebot
from telebot import types
from config import BOT_TOKEN
from vigenere_chipher import main_decode, main_encode, get_dict
from caesar_chipher import caesar_encode, caesar_decode

bot = telebot.TeleBot(BOT_TOKEN)  # токен
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton('Зашифровать сообщение')
btn2 = types.KeyboardButton('Расшифровать сообщение')
btn3 = types.KeyboardButton('О боте')
markup.add(btn1, btn2, btn3)
decode_or_encode = 0  # Указывает что сделать с текстом, если == 1 - зашифровать если == 2 - расшифровать


@bot.message_handler(commands=['start'])
def start(message):
    '''
    Обрабатывает команду /start, отправляет приветственное сообщение, добавляет клавиши.
    '''
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nЧем могу помочь?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    '''
    Обрабатывает команду /help.
    '''
    bot.send_message(message.chat.id,
                     f'Бот умеет зашифровывать и расшифровывать текст на латинице с помощью шифра Цезаря и шифра Виженера. Бот создан в качестве итогового проекта по дисциплине АиП. Словарь допустимых символов: {get_dict()}')


@bot.message_handler(content_types=['text'])
def mess(message):
    '''
    Обрабатывает пользовательский ввод.
    '''
    get_messsage_bot = message.text.strip().lower()
    global decode_or_encode

    if get_messsage_bot == "назад":
        start(message)
    elif get_messsage_bot == "зашифровать сообщение":
        decode_or_encode = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Шифр Виженера')
        btn2 = types.KeyboardButton('Шифр Цезаря')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        final_message = "Выберите метод шифрования"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_messsage_bot == 'шифр виженера' and decode_or_encode == 1:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,
                         'Текст должен быть на латинице, возможно использование цифр и специальных символов!',
                         parse_mode='html', reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Введите текст для шифрования:</b>', parse_mode='html',
                         reply_markup=markup)

        def add_text(message):
            '''
            Получает пользовательский текст.
            '''
            text = message.text
            bot.send_message(message.chat.id, '<b>Введите секретный ключ:</b>', parse_mode='html')

            def add_key(message):
                '''
                Получает ключ от пользователя и отправляет зашифрованый текст.
                '''
                global markup
                key = message.text
                msg_to_user = main_encode(text, key)
                bot.send_message(message.chat.id, msg_to_user, parse_mode='html', reply_markup=markup)

            bot.register_next_step_handler(message, add_key)

        bot.register_next_step_handler(message, add_text)
    elif get_messsage_bot == 'шифр цезаря' and decode_or_encode == 1:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,
                         'Текст должен быть на латинице, возможно использование цифр и специальных символов!',
                         parse_mode='html', reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Введите текст для шифрования:</b>', parse_mode='html',
                         reply_markup=markup)

        def add_text(message):
            '''
            Получает пользовательский текст.
            '''
            text = message.text
            bot.send_message(message.chat.id, '<b>Введите сдвиг:</b>', parse_mode='html')

            def add_key(message):
                '''
                Получает от пользователя число на которое нужно сдвинуть текст и отправляет зашифрованное сообщение.
                '''
                global markup
                key = message.text
                msg_to_user = caesar_encode(text, int(key))
                bot.send_message(message.chat.id, msg_to_user, parse_mode='html', reply_markup=markup)

            bot.register_next_step_handler(message, add_key)

        bot.register_next_step_handler(message, add_text)
    elif get_messsage_bot == "расшифровать сообщение":
        decode_or_encode = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Шифр Виженера')
        btn2 = types.KeyboardButton('Шифр Цезаря')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        final_message = "Выберите метод шифрования"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_messsage_bot == 'шифр виженера' and decode_or_encode == 2:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,
                         'Текст должен быть на латинице, возможно использование цифр и специальных символов!',
                         parse_mode='html', reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Введите текст для расшифрования:</b>', parse_mode='html',
                         reply_markup=markup)

        def add_text(message):
            '''
            Получает пользовательский текст.
            '''
            text = message.text
            bot.send_message(message.chat.id, '<b>Введите секретный ключ:</b>', parse_mode='html')

            def add_key(message):
                '''
                Получает от пользователя секретный ключ и отправляет пользователю расшифрованное сообщение.
                '''
                global markup
                key = message.text
                msg_to_user = main_decode(text, key)
                bot.send_message(message.chat.id, msg_to_user, parse_mode='html', reply_markup=markup)

            bot.register_next_step_handler(message, add_key)

        bot.register_next_step_handler(message, add_text)
    elif get_messsage_bot == 'шифр цезаря' and decode_or_encode == 2:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,
                         'Текст должен быть на латинице, возможно использование цифр и специальных символов!',
                         parse_mode='html', reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Введите текст для расшифрования:</b>', parse_mode='html',
                         reply_markup=markup)

        def add_text(message):
            '''
            Получает от пользователя текст.
            '''
            text = message.text
            bot.send_message(message.chat.id, '<b>Введите сдвиг:</b>', parse_mode='html')

            def add_key(message):
                '''
                Получает от пользователя число на которое нужно сдвинуть текст и отправляет расшифрованное сообщение.
                '''
                global markup
                key = message.text
                msg_to_user = caesar_decode(text, int(key))
                bot.send_message(message.chat.id, msg_to_user, parse_mode='html', reply_markup=markup)

            bot.register_next_step_handler(message, add_key)

        bot.register_next_step_handler(message, add_text)
    elif get_messsage_bot == 'о боте':
        help(message)


# bot.infinity_polling()
bot.polling(none_stop=True)
