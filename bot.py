# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
#def handle_start_help(message):
#    pass
def firstcall(message):
    bot.send_message(message.chat.id, "Hi, my name is ORTBot. What's yours?")


@bot.message_handler(commands=['help'])
def ht(message):
    bot.send_message(message.chat.id, "I've lost my Guru, srry! :'(")


@bot.message_handler(content_types=["text"])

#def repeat_all_messages(message): 
 #   bot.send_message(message.chat.id, message.text)
def hiba(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "Hi, H0bb1t")
    elif message.text == "Bye":
        bot.send_message(message.chat.id, "Bye, H0bb1t")
    else:
        bot.send_message(message.chat.id, "Can't understand u!")


        

if __name__ == '__main__':
     bot.polling(none_stop=True)


