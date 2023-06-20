import pyttsx3
import datetime
import requests
from playsound import playsound

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    # print(voices)
    # print(voices[4].id)
    engine.setProperty('rate', 200)
    print("")
    print(f"AI : {Text}.")
    print("")
    engine.say(Text)
    # engine.save_to_file('')
    engine.runAndWait()

def Weather():
    try:
        # API_ID = "6bdc65b2712df413f9c8c024944dddb8"

        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "6bdc65b2712df413f9c8c024944dddb8"
        CITY = "dewas"
        CITY = CITY.replace(' ', '')
        CITY = CITY.replace('now', '')


        # CITY = 'Dewas'

        def kelvin_celsius(kelvin):
            celcius = kelvin - 273.15
            return celcius


        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_celsius(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius = kelvin_celsius(feels_like_kelvin)
        humidity = response['main']['humidity']
        pressure = response['main']['pressure']
        visibility = response['visibility'] / 1000
        # rain = response['weather']['rain']
        # clouds = response['main']['clouds']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description']
        sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        speak(f"Today Temperature is : {temp_celsius:.2f}ºCelcius")

        speak(f"Today Temperature feels like : {feels_like_celsius:.2f}ºCelcius")

        speak(f"Humidity is : {humidity}% ")

        speak(f"Pressure is : {pressure} hecto Pascals or millibars ")

        speak(f"Visibility is : {visibility} kilometer ")

        speak(f"Wind Speed is : {wind_speed} kilometer per hour ")

        speak(f"General Weather is : {description} ")

        speak(f"Sun Rises at {sunrise_time} local time")

        speak(f"Sun Set at {sunset_time} local time ")

    except:
        speak('Sorry, i did not understand the city name.')


def Alarm():
    alarmHour = 2
    alarmMinute = 28
    alarmAmPm = "pm"
    if alarmAmPm == "pm":
        alarmHour += 12
    while True:
        if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
            speak("Wake Up Neeraj")
            speak('')
            speak('Good Morning.')
            speak('')
            Weather()
            speak('')
            speak('Again, Good Morning Sir.')
            break

# Alarm()