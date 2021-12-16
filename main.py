import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Зашифровать сообщение')
    btn2 = types.KeyboardButton('Расшифровать сообщение')
    btn3 = types.KeyboardButton('О боте')
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nЧем могу помочь?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_messsage_bot = message.text.strip().lower()

    if get_messsage_bot == "назад":
        start(message)
    elif get_messsage_bot == "зашифровать сообщение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Шифр Виженера')
        btn2 = types.KeyboardButton('Шифр Цезаря')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        final_message = "Выберите метод шифрования"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_messsage_bot == 'шифр виженера':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,'Текст должен быть на латинице, возможно использование цифр и специальных символов!',parse_mode='html', reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Введите текст для шифрования:</b>', parse_mode='html',reply_markup=markup)
        def add_text(message):
            text = message.text
            bot.send_message(message.chat.id, '<b>Введите секртеный ключ:</b>', parse_mode='html',
                             reply_markup=markup)

            print(text)
        bot.register_next_step_handler(message, add_text)


# bot.infinity_polling()
bot.polling(none_stop=True)
