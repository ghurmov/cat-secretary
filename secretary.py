import telebot
import time
from telebot import types
import datetime as dt
import schedule
import os

token = '648003914:AAGo7q_ucIqh0DYAV-0cD90fIm3IFuS5qGw'
bot = telebot.TeleBot(token=token)




'''
markup = types.ReplyKeyboardMarkup(row_width = 2)
button1 = types.KeyboardButton ('мяу')
button2 = types.KeyboardButton ('мурр')
markup.add(button1,button2)

mar2 = types.ReplyKeyboardRemove



@bot.message_handler(content_types=['text'])
def mes(message):
    if message.text != 'meow':

        bot.send_message(message.chat.id, 'do it',reply_markup=markup)
        bot.edit_message_reply_markup(message.chat.id, message, reply_markup=mar2)


    if message.text == 'meow':
        #but1 = types.KeyboardButton ('окончательный мурр')
        #but2 = types.KeyboardButton('окончательный мяу')
       # bot.send_message(message.chat.id, 'о вы от мяуыча', reply_markup=mar2)
       bot.send_message(message.chat.id, '-----')
''' # other



time.strftime('%X %x %Z')
'12:45:20 08/19/09 CDT'
os.environ['TZ'] = 'Europe/Moscow'
time.tzset()
time.strftime('%X %x %Z')
'18:45:39 08/19/09 BST'

year = time.strftime('%Y')
month = time.strftime('%m')
day = time.strftime('%d')
hour = time.strftime('%H')
minute = time.strftime('%M')
print (type(hour))

def timecheck():
    while True:
        hour = time.strftime('%H')
        minute = time.strftime('%M')

        print (hour + ':' + minute)

        if int(hour) == 17 and int(minute) == 15:
            print ('ALARM!')
            napalarm()
        if int(hour) == 7 and int(minute) == 20:
            napalarm()
        if int(hour) == 12 and int(minute) == 20:
            napalarm()
        if int(hour) == 18 and int(minute) == 10:
            napalarm()
        if int(hour) == 23 and int(minute) == 45:
            corealarm()


        time.sleep(10)

def napalarm():
    bot.send_message(120862745, 'Nap!')
    time.sleep(60)
def corealarm():
    bot.send_message(120862745, 'Get ready for bed')
    time.sleep(60)

timecheck()


while True:
    try:
        bot.polling()
    except Exception:
        bot.stop_bot()
        time.sleep(15)
        bot.polling()