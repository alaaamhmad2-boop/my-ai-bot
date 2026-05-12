import telebot
from telebot import types
import google.generativeai as genai
import os
import requests
import random

# --- مفاتيح إبراهيم الخاصة ---
TOKEN = "8725135675:AAGElolme9Zm2d3Kq7xoYxdhWwad1kLhu9I"
GEMINI_KEY = "AIzaSyBl90Z2S-O-jXQ2vVw8v8v8v8v8v8v8v8" 

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

def main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("📸 تحسين الصور", "💬 محادثة مفتوحة", "🤖 مهارات الذكاء الاصطناعي", "🛠 المساعدة والدعم", "💡 نصيحة أخوية")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "أهلاً يا مهندس إبراهيم! البوت شغال الآن 24/7.", reply_markup=main_markup())

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    if message.text == "💡 نصيحة أخوية":
        bot.reply_to(message, "يا إبراهيم: المهندس الحقيقي هو من يصنع الحلول من العدم. استمر في طريقك.")
    else:
        try:
            response = model.generate_content(message.text)
            bot.reply_to(message, response.text)
        except:
            bot.reply_to(message, "أنا معك، اسألني مرة أخرى.")

if __name__ == "__main__":
    bot.infinity_polling()
