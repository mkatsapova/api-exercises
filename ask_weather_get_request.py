"""to get the weather for the city/town from the web site using API and save the results to the JSON file"""

import datetime
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def ask_weather():
    try:
        city_name = input('Please, enter the city or town name: ')
        params = {'q': f'{city_name}', 'appid': os.getenv('API_TOKEN'), 'units': 'metric'}
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

        weather_data = response.json()
        print(f'The {weather_data["name"]}, locality {weather_data["sys"]["country"]}\n'
              f'The temperature is {weather_data["main"]["temp"]}°C\n'
              f'Feels like {weather_data["main"]["feels_like"]}°C\n'
              f'Pressure is {weather_data["main"]["pressure"]}hpa\n'
              f'Humidity is {weather_data["main"]["humidity"]}%\n'
              f'Wind speed is {weather_data["wind"]["speed"]}m/s\n'
              f'Clouds {weather_data["clouds"]["all"]}%\n'
              f'Rainfall: {weather_data["weather"][0]["description"]}')
        # print(response.json())
        new_data = {f'{datetime.datetime.now()}': f'{weather_data}'}
        try:
            with open('data_file.json') as file:
                data = json.load(file)
        except:
            data_file = {"weather": []}
            filename = 'data_file.json'
            with open(filename, 'w') as f:
                json.dump(data_file, f)
            with open('data_file.json') as file:
                data = json.load(file)
        data['weather'].append(new_data)
        with open('data_file.json', 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
    except:
        print('Ooops... something went wrong, sorry dear!')


if __name__ == '__main__':
    ask_weather()
