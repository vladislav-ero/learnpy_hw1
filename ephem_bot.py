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

def get_constel(bot, update):
    today = str(date.today().strftime("%Y/%m/%d"))
    
    # planets = {"Mercury": ephem.Mercury(today), 
    # "Venus": ephem.Venus(today), 
    # "Mars" : ephem.Mars(today), 
    # "Jupiter": ephem.Jupiter(today), 
    # "Saturn": ephem.Saturn(today), 
    # "Uranus": ephem.Uranus(today), 
    # "Neptune": ephem.Neptune(today)}

    planet_input = str(update.message.text.split()[1]).lower().capitalize()

    if planet_input == "Mercury":
        mercury = ephem.Mercury(today)
        mercury_const = ephem.constellation(mercury)[1]
        planet_output = f"Mercury is in {mercury_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Venus":
        venus = ephem.Venus(today)
        venus_const = ephem.constellation(venus)[1]
        planet_output = f"Venus is in {venus_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Mars":
        mars = ephem.Mars(today)
        mars_const = ephem.constellation(mars)[1]
        planet_output = f"Mars is in {mars_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Jupiter":
        jupiter = ephem.Jupiter(today)
        jupiter_const = ephem.constellation(jupiter)[1]
        planet_output = f"Jupiter is in {jupiter_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Saturn":
        saturn = ephem.Saturn(today)
        saturn_const = ephem.constellation(saturn)[1]
        planet_output = f"Saturn is in {saturn_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Uranus":
        uranus = ephem.Uranus(today)
        uranus_const = ephem.constellation(uranus)[1]
        planet_output = f"Uranus is in {uranus_const}"
        update.message.reply_text(planet_output)

    if planet_input == "Neptune":
        neptune = ephem.Neptune(today)
        neptune_const = ephem.constellation(neptune)[1]
        planet_output = f"Neptune is in {neptune_const}"
        update.message.reply_text(planet_output) 

    # if planet_input in planets:
    #     print(ephem.constellation(planets[planet_input]))

    
    
    # day = str(date.today()).split("-")
    # print(day)

    # today = f"{day[0]}/{day[1]}/{day[2]}"
    # print("Today's date:", today)
    # print(planet_input)
    # update.message.reply_text("Today's date:", today)
    # update.message.reply_text(planet_input)

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
    dp.add_handler(CommandHandler("planet", get_constel))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
