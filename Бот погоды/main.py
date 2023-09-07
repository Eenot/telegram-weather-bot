import telebot
from telebot import types
#import datetime    
from datetime import date
import requests
from bs4 import BeautifulSoup as bs

token = ""
x = current_date = date.today()
dat =   "Погода на " + str(current_date.day)+ "." + str(current_date.month) + "." + str(current_date.year)
bot= telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Что может бот?")
    btn1 = types.KeyboardButton("Посмотреть погоду")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот прогноза погоды по городам".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Выберите желаемую функцию!", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):

    if message.text == "Что может бот?":
        bot.send_message(message.chat.id, text="Показывать погоду по городам России")
    elif (message.text == "Посмотреть погоду"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        pogodusm = types.KeyboardButton("Москва")
        pogoduss = types.KeyboardButton("Санкт-Петербург")
        pogodussoch = types.KeyboardButton("Сочи")
        pogodusa = types.KeyboardButton("Архыз")
        pogodusb = types.KeyboardButton("Казань")
        pogodusan = types.KeyboardButton("Калининград")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(pogodussoch,pogoduss,pogodusm,pogodusa,pogodusb,pogodusan,back)
        bot.send_message(message.chat.id, text="Выберите город, погоду в котором желаете посмотреть.", reply_markup=markup)
    elif (message.text == "Москва"):
        url = "https://weather.rambler.ru/v-moskve/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n" 
        bot.send_photo(message.chat.id, 'https://imgur.com/a/T2dSWA3', itog)  
        #bot.send_message(message.chat.id, itog)

    elif (message.text == "Санкт-Петербург"):
        url = "https://weather.rambler.ru/v-sankt-peterburge/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n"
        bot.send_photo(message.chat.id, 'https://imgur.com/a/R9u2qGv', itog)
        #bot.send_message(message.chat.id, itog)
    elif (message.text == "Сочи"):
        url = "https://weather.rambler.ru/v-sochi/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n"
        bot.send_photo(message.chat.id, 'https://imgur.com/a/xxBrNOU', itog)
        #bot.send_message(message.chat.id, itog)
    elif (message.text == "Архыз"):
        url = "https://weather.rambler.ru/v-arkhyze/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n"
        bot.send_photo(message.chat.id, 'https://imgur.com/a/Hqz9oBW', itog)
        #bot.send_message(message.chat.id, itog)
    elif (message.text == "Казань"):
        url = "https://weather.rambler.ru/v-kazani/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n"
        bot.send_photo(message.chat.id, 'https://imgur.com/a/jgWKQZx', itog)
        #bot.send_message(message.chat.id, itog)
    elif (message.text == "Калининград"):
        url = "https://weather.rambler.ru/v-kaliningrade/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        weather = soup.find('div',  class_ = 'HhSR MBvM')
        weather1 = soup.find('div', class_='TWnE')
        weathers = soup.find_all('span', class_='VaOz PB4k')
        itog = dat + "\nТемпература воздуха: " + weather.text + "\n" + weather1.text  + "\n"
        for weather2 in weathers:
            itog = "\n" + itog + "\n" + weather2.text + "\n"
        bot.send_photo(message.chat.id, 'https://imgur.com/a/A67mup5',itog)
        #bot.send_message(message.chat.id, itog)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Что может бот?")
        btn1 = types.KeyboardButton("Посмотреть погоду")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню. \nВыберите функцию.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Такого я не умею")
bot.infinity_polling()