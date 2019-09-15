"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from datetime import date

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def answer_planet(bot, update):
    user_text = update.message.text.split() 
    try:
        planet = user_text[1].lower().capitalize()
    except IndexError:
        update.message.reply_text("Вы не ввели название планеты после /planet")       
    today = date.today().strftime('%Y/%m/%d')
    logging.info(f"User: {update.message.chat.username}, Message: {update.message.text}, Planet: {planet}")
    try:
        get_planet = getattr(planet, ephem)(today)
    except AttributeError:
        update.message.reply_text("Я не могу определить, в каком созвездии ваша планета, или вы ввели не название планеты.")
    const = ephem.constellation(get_planet)
    update.message.reply_text(f"Сегодня {planet} находится в созвездии {const[1]}.")

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
API_KEY = None
with open("token.txt") as f:
    API_KEY = f.read().strip()

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", answer_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
