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


bot.infinity_polling()
