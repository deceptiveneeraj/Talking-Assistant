import pyttsx3
import webbrowser as web
import time
import keyboard
import smtplib
import os
from PIL import Image
import datetime as dt
import requests
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[3].id)
Assistant.setProperty('rate', 200)

# Speak
def speak(text):
    print("   ")
    Assistant.say(text)
    print(f" {text}")
    print("   ")
    Assistant.runAndWait()


# Speedtest
def SpeedTest(query):
    query = str(query).lower()

    import speedtest
    speak('I am checking internet speed, wait a minute sir...')
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading / 800000)
    uploading = speed.upload()
    correctUpload = int(uploading / 800000)

    if 'downloading' in query:
        speak(f"The downloading speed is {correctDown} mbps")
    elif 'uploading' in query:
        speak(f"The uploading speed is {correctUpload} mbps")
    else:
        speak(f"The downloading speed is {correctDown} mbps and The uploading speed is {correctUpload} mbps")


# Whatsapp.
def whatsapp_msg(number, message):
    try:
        num = '+91' + number
        open_chat = "https://web.whatsapp.com/send?phone=" + num
        web.open(open_chat)
        time.sleep(15)
        keyboard.write(message)
        time.sleep(1)
        keyboard.press('enter')
        speak('Message Send.')
    except:
        speak('Try Again...')


def whatsapp_grp(group_id, message):
    try:
        open_chat = "https://web.whatsapp.com/accept?code=" + group_id
        web.open(open_chat)
        time.sleep(15)
        keyboard.write(message)
        time.sleep(1)
        keyboard.press('enter')
        speak('Message Send.')
    except:
        speak('Try Again...')


'''def whatsapp():
    speak('Tell me the name of the person.')
    name = takecommand()
    #elif 'time' in query:
    #    time = datetime.datetime.now().strftime('%I:%M %p')
    #    print(time)
    #    speak('Current Time Is ' + time)


    if 'vinita' in name:
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg('+9162*********', msg, hour, min, 20)
        speak('Whats app message send.')

    elif 'ritesh' in name:
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+918***********", msg, hour, min, 20)
        speak('Whats app message send.')

    else:
        speak('Tell me the phone number.')
        phone = int(takecommand())
        ph = '+91' + phone
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        speak('Whats app message send.')
        pywhatkit.sendwhatmsg()'''

# Send Email.
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        with open("C:\\Users\\neera\\PycharmProjects\\ADatabase\\API\\GmailPass.txt", "r") as password_file:
            Password = password_file.read().strip()
        server.login('neerajsolanki271@gmail.com', Password)
        server.sendmail('neerajsolanki271@gmail.com', to, content)
        server.close()
        speak('Email send successfully.')
    except Exception as e:
        print(e)
        speak('Try Again...')


# Nasa
API_KEY = open("C:\\Users\\neera\\PycharmProjects\\ADatabase\\API\\NasaNewsApi.txt", "r")
Api_Key = API_KEY
def NasaNews(Date):
    try:
        speak('Extracting data from NASA')
        url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
        Params = {'date': str(Date)}
        r = requests.get(url, params=Params)
        Data = r.json()
        Info = Data['explanation']
        Title = Data['title']
        Image_Url = Data['url']
        Image_r = requests.get(Image_Url)
        FileName = str(Date) + '.jpg'
        with open(FileName, 'wb') as f:
            f.write(Image_r.content)
        Path_1 = "C:\\Users\\neera\\PycharmProjects\\AI Friday\\" + str(FileName)
        Path_2 = "C:\\Users\\neera\\PycharmProjects\\AI Friday\\Data\\Nasa Data Base\\" + str(FileName)
        os.rename(Path_1, Path_2)
        img = Image.open(Path_2)
        img.show()
        speak(f"Title : {Title}")
        speak(f"According to Nasa : {Info}")
        os.remove("C:\\Users\\neera\\PycharmProjects\\AI Friday\\Data\\Nasa Data Base\\" + str(FileName))
    except:
        speak('I did not understand can you say it again please')

# NasaNews('2020-11-02')

def SolarBody(body):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    r = requests.get(url)
    Data = r.json()
    bodies = Data['bodies']
    Number = len(bodies)
    url2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
    R = requests.get(url2)
    data2 = R.json()
    mass = data2['mass']['massValue']
    volume = data2['vol']['volValue']
    density = data2['density']
    gravity = data2['gravity']
    escape = data2['escape']
    eccentricity = data2['eccentricity']

    speak(f"Number of Bodies in Solar System : {Number}.")
    speak(f"Mass Of {body} is {mass} kilogram.")
    speak(f"Eccentricity of {body} is {eccentricity}")
    speak(f"Density Of {body} is {density} kg per meter cube")
    speak(f"Gravity Of {body} is {gravity} newton.")
    speak(f"Escape Velocity of {body} is {escape} meter per second")

"""{'id': 'terre', 'name': 'La Terre', 'englishName': 'Earth', 'isPlanet': True,
 'moons': [{'moon': 'La Lune', 'rel': 'https://api.le-systeme-solaire.net/rest/bodies/lune'}],
  'semimajorAxis': 149598023, 'perihelion': 147095000, 'aphelion': 152100000, 'eccentricity': 0.0167,
   'inclination': 0, 'mass': {'massValue': 5.97237, 'massExponent': 24}, 'vol': {'volValue': 1.08321, 'volExponent': 12},
    'density': 5.5136, 'gravity': 9.8, 'escape': 11190.0, 'meanRadius': 6371.0084, 'equaRadius': 6378.1366, 
    'polarRadius': 6356.8, 'flattening': 0.00335, 'dimension': '', 'sideralOrbit': 365.256, 'sideralRotation': 23.9345,
     'aroundPlanet': None, 'discoveredBy': '', 'discoveryDate': '', 'alternativeName': '', 'axialTilt': 23.4393, 
     'avgTemp': 288, 'mainAnomaly': 358.617, 'argPeriapsis': 85.901, 'longAscNode': 18.272, 'bodyType': 'Planet'}
"""
# SolarBody('pluto')

# Weather Report
"""
{'coord': {'lon': 76.0667, 'lat': 22.9667}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}],
 'base': 'stations', 'main': {'temp': 295.25, 'feels_like': 294.53, 'temp_min': 295.25, 'temp_max': 295.25, 
 'pressure': 1011, 'humidity': 39, 'sea_level': 1011, 'grnd_level': 949}, 'visibility': 10000, 
 'wind': {'speed': 3.44, 'deg': 287, 'gust': 5.6}, 'clouds': {'all': 0}, 'dt': 1671799684, 
 'sys': {'type': 1, 'id': 9067, 'country': 'IN', 'sunrise': 1671759176, 'sunset': 1671797774}, 
 'timezone': 19800, 'id': 1273066, 'name': 'Dewas', 'cod': 200}
"""
def WeatherReport():
    try:
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        Api_Key = open("C:\\Users\\neera\\PycharmProjects\\ADatabase\\API\\WeatherApi.txt", "r").read().strip()
        CITY = 'Dewas'

        def kelvin_celsius(kelvin):
            celcius = kelvin - 273.15
            return celcius

        url = BASE_URL + "appid=" + Api_Key + "&q=" + CITY
        response = requests.get(url).json()


        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_celsius(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius = kelvin_celsius(feels_like_kelvin)
        min_kelvin = response['main']['temp_min']
        min_celsius = kelvin_celsius(min_kelvin)
        min_kelvin = response['main']['temp_max']
        max_celsius = kelvin_celsius(min_kelvin)
        humidity = response['main']['humidity']
        pressure = response['main']['pressure']
        visibility = response['visibility'] / 1000
        # rain = response['weather']['rain']
        # clouds = response['main']['clouds']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        sea_level = response['main']['sea_level']

        speak(f"Temperature in {CITY} is : {temp_celsius:.2f}ºCelcius")

        speak(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}ºCelcius")

        speak(f"The Minimum Temperature in {CITY} is : {min_celsius:.2f}ºCelcius")

        speak(f"The Maximum Temperature in {CITY} is : {max_celsius:.2f}ºCelcius")

        speak(f"Humidity in {CITY} is : {humidity}% ")

        speak(f"Pressure in {CITY} is : {pressure} hecto Pascals or millibars ")

        speak(f"Visibility in {CITY} is : {visibility} kilometer ")

        speak(f"Wind Speed in {CITY} is : {wind_speed} kilometer per hour ")

        speak(f"General Weather in {CITY} is : {description} ")

        speak(f"Sun Rises in {CITY} at {sunrise_time} local time")

        speak(f"Sun Set in {CITY} at {sunset_time} local time ")

        speak(f"Sea Level in {CITY} is : {sea_level}")
    except:
        speak('Sorry, i did not understand the city name.')
# WeatherReport()

