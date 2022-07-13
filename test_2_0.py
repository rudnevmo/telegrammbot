import datetime
import requests
from pprint import pprint
from config import tg_token_bot, open_weather_token, weather_2


def get_weather(city, open_weather_token):
    try:
        smile = {
            'Clear': 'Ясно \U0001F31E',
            'Clouds': 'Хмарно \U0001F325',
            'Rain': 'Дощ \U0001F327',
            'Drizzle': 'Дощ \U0001F327',
            'Thunderstorm': 'Гроза \U0001F329',
            'Snow': 'Сніг \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }
        h = requests.get(
             f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric&lang=ua'
        )
        data_weather = h.json()
        pprint(data_weather)
        city = data_weather['city']['name']
        cut_weather = data_weather['list'][0]['main']['temp']
        weather_des = data_weather['list'][1]['weather'][0]['main']
        if weather_des in smile:
            wd = smile[weather_des]
        else:
            wd = 'Визерни у вікно, я не розумію що там коїться'
        feel_temp = data_weather['list'][0]['main']['feels_like']
        pressure = data_weather['list'][0]['main']['pressure']
        humidity = data_weather['list'][0]['main']['humidity']
        precipitation = data_weather['list'][0]['pop']
        wind = data_weather['list'][0]['wind']['speed']
        message_wind = ''
        if wind > 10.8:
            message_wind = '. Будь обережним на вулиці, вітер сильний'
        elif wind < 10.8:
            pass
        messag_atent = 'Have a nice day \U0001F609'
        if weather_des == 'Rain' or weather_des == 'Drizzle':
            messag_atent = 'Не заудь парасольку \U00002614'
        elif weather_des == 'Thunderstorm':
            messag_atent = 'Не перебувай на відкриій місцевості та не ховайся під деревами, а кращу посидь вдома ' \
                           '\U0001F329'
        elif weather_des == 'Snow':
            messag_atent = 'Будь обережним на вулиці \U00002744'
        elif weather_des == 'Mist':
            messag_atent = 'Будь обережним за кермом \U0001F301'
        print(f'***{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}***\n'
              f'Погода в {city}:\nТемпратура: {cut_weather}°C, відчувається як: {feel_temp}°C\n{wd}\n'
              f'Атмосферний тиск: {pressure} мм.рт.ст\nВідносна вологість: {humidity}%\nЙмовірність опадів на '
              f'сьогодні: {precipitation * 100}%\nШвидкість вітру:{wind} м/с {message_wind}\n{messag_atent}')
    except:
        print('\U0000203C Перевірте назву міста \U0000203C')


def main():
    city = input('Введіть місто: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
