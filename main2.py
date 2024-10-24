import telebot as t
import requests
import json

bot = t.TeleBot("Your_Token")
WeatherAPI = "Your_Token" #Openweather.com token*
print("Bot successfully started!")
@bot.message_handler(commands=["start", "restart"])
def start(message):
    bot.send_message(message.chat.id, f"Привет {message.chat.first_name}. Напиши название города\nи я скажу тебе какая там температура 🌡")

@bot.message_handler(content_types=["text"])
def getw(message):
    try:
        city = message.text.strip().lower()
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI}&units=metric")
        data = json.loads(res.text)
        bot.send_message(message.chat.id, f"Сейчас в городе {data["main"]["temp"]} градуса.\nЕсли хотите узнать про другой город, напиши мне!")
    except Exception:
        bot.send_message(message.chat.id, "Неверный город, введите город заново")
        bot.register_next_step_handler(message, getw)
bot.polling(none_stop=True)
