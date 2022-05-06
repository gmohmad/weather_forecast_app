import os
from posixpath import split

import requests
from telegram.ext import (
    CommandHandler,
    Filters,
    MessageHandler,
    Updater
)

from utils import ChatBot

BASE_API_ENDPOIND = 'http://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
APP_ID = 'b21a2633ddaac750a77524f91fe104e7'

PORT = int(os.environ.get('PORT', '8443'))
TELEGRAM_TOKEN = '5362702089:AAHw5AYgX2WMQv8Y4xt8QVyQy7J24ixQxzc'
APP_NAME = 'https://weather-tg-chatbot.herokuapp.com/'

chatbot = ChatBot()


def start(update, context):
    chatbot.start()
    update.message.reply_text(
        ' '.join('Hi👋🏻 Here you can check the weather forecast! Enter \
            your city 🌆, the temperature 🌡 that is comfortable for you and \
            the weather 🌦 that you like best'.split())
    )

    update.message.reply_text('Enter your city 🌆')


def stop(update, context):
    chatbot.stop()
    update.message.reply_text('To get started, enter the command /start')


def conversation(update, context):
    message = update.message.text.lower()

    if chatbot.state == 'get city':
        url = BASE_API_ENDPOIND + f'?q={message}&units={UNITS}&appid={APP_ID}'
        weather_response = requests.get(url).json()

        if weather_response.get('message') == 'city not found':
            update.message.reply_text('City not found 😕. Please try again 😊!')

        else:
            chatbot.city = message.title()
            chatbot.weather_api_response = weather_response

            chatbot.get_comfortable_temperature()
            update.message.reply_text('Enter a comfortable temperature for you 🌡')


    elif chatbot.state == 'get comfortable temperature':

        if (message.startswith('-') and message[1:].isdigit()) or message.isdigit():
            chatbot.comfortable_temperature = message

            chatbot.confirm()
            update.message.reply_text(
                ' '.join(f'Your city is {chatbot.city}, is the temperature \
                comfortable for you - {chatbot.comfortable_temperature} degrees? Please confirm'.split())
            )

        else:
            update.message.reply_text('Must be entered in numeric format 🔢. Please try again 😊!')


    elif chatbot.state == 'confirm':

        if message == 'yes' or message == 'да':
            chatbot.end()

            current_temperature = chatbot.weather_api_response.get('main', {}).get('temp')
            current_weather = chatbot.weather_api_response.get('weather')[0].get('description')

            update.message.reply_text('Thank you 😊!')
            update.message.reply_text(f'Your city 🌆 is {chatbot.city}')
            update.message.reply_text(f'The current temperature 🌡 is {current_temperature} degrees')
            update.message.reply_text(f'The current weather 🌦 is {current_weather}')

            if int(chatbot.comfortable_temperature) == current_temperature:
                update.message.reply_text('The current temperature is comfortable for you 😁🎉')
            else:
                update.message.reply_text('The current temperature is not comfortable for you 😔🥺')

            update.message.reply_text('To start over, enter the command /start')

        elif message == 'no' or message == 'нет':
            chatbot.end()
            update.message.reply_text('To start over, enter the command /start')

        else:
            update.message.reply_text(
                ' '.join('You must either confirm or not confirm. If you change your mind \
                about watching the weather, enter the command /stop'.split())
            )

            update.message.reply_text(
                ' '.join(f'Your city is {chatbot.city}, is the temperature \
                comfortable for you - {chatbot.comfortable_temperature} degrees? Please confirm'.split())
            )


if __name__ == '__main__':
    updater = Updater(TELEGRAM_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(MessageHandler(Filters.text, conversation))

    updater.start_polling()

    # For deploy on heroku
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TELEGRAM_TOKEN, webhook_url=APP_NAME + TELEGRAM_TOKEN)
    # updater.idle()
