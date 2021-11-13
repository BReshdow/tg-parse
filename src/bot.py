import telebot
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from weather import temperature

# Initializing bot
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # Creating a reply markup
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Погода сегодня')
    markup.add(btn1)

    # Greeting user
    hello_msg = f'{message.from_user.first_name}, привет!'
    bot.send_message(message.chat.id, hello_msg, reply_markup=markup)


# Messages handler
@bot.message_handler(content_types=['text'])
def weather(message):
    # Send weather information
    if message.text in ['Погода сегодня', '/weather']:
        if temperature:
            bot.send_message(message.chat.id, temperature)
        else:
            bot.send_message(message.chat.id, 'К сожалению, произошла ошибка😢')
    # Else send message
    else:
        bot.send_message(message.chat.id,
                         'Я не знаю что на это ответить😔')


# Running
bot.polling(none_stop=True)
