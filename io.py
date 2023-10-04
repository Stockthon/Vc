
import telebot

import os

os.system("pip install telebot")


# قم بتعيين توكن البوت الخاص بك هنا
TOKEN = '6067746005:AAFMF-jUwwzGj71obCOb9V217oEy_BWq_UQ'

# إنشاء كائن bot
bot = telebot.TeleBot(TOKEN)

# تعريف الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك! أهلاً بك في البوت.")

# تشغيل البوت
bot.polling()
