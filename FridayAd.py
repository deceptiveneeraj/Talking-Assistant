import speech_recognition as sr
import pyttsx3
import time
from time import sleep
import datetime
import datetime as dt
import pywhatkit
import keyboard
from keyboard import press_and_release
from keyboard import press
from keyboard import write
import random
import wikipedia
import webbrowser
import webbrowser as web
import os
from os import startfile
from playsound import playsound
import mss
import cv2
import requests
from requests import get
import numpy as np
import pyautogui
from pyautogui import click
import smtplib
import pyjokes
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pyscreenshot as ImageGrab
from googletrans import Translator
import wolframalpha
from PIL import Image

from Features import OpenAndClose
from Features import FeaturesAndTasks


# .............Brain............. #
# ............................... #
from Brain.AIBrain import ReplyBrain
from Brain.QNA import QuestionAnswer

# ............ChatBot............ #
# ............................... #
from ChatBot.ChatBot import TaskExecution

# .............Speak............. #
# ............................... #
def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    # print(voices)
    # print(voices[5].id)
    engine.setProperty('rate', 200)
    print("")
    print(f"AI : {Text}.")
    print("")
    engine.say(Text)
    # engine.save_to_file('')
    engine.runAndWait()


# .............Listen............. #
# ................................ #
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listen...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
#       audio = r.listen(source)

        try:
            print("Recognize...")
            query = r.recognize_google(audio, language="hi")

        except:
            return ""
        query = str(query).lower()
        return query
# print(Listen())

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You Said: {data}")
    return data
# TranslationHinToEng("फ्राइडे तुम क्या कर रही हो")

def takecommand():
    query = Listen()
    data = TranslationHinToEng(query)
    return data


# ................................................................................................................#
# ................................................................................................................#
# ................................................................................................................#

def TaskExe():
# While True Execution All Statement.
    while True:

        query = takecommand()
        query = str(query).lower()

        # Play anything on YouTube.
        if 'play' in query:
            song = query.replace('play', '')
            speak('Playing...' + song)
            pywhatkit.playonyt(song)
            speak('Playing...')
            print('Playing...')
            break

        # Time, Date, Temperature
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current Time Is ' + time)
            break

        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d-%m-%Y')
            print(date)
            speak('Today date is ' + date)
            break

        elif 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"Today {day}")

        elif 'temperature' in query:
            try:
                speak('Tell Me The City Name.')
                City = takecommand().lower()
                City = City.replace(' ', '')
                url = f"https://www.google.com/search?q=temperature+in+{City}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current temperature in {City} is {temp}")
                print(f"current temperature in {City} is {temp}")
                break
            except:
                speak('Sorry, i did not understand the city name.')
                break

        elif 'good morning' in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour <= 11:
                speak('Good Morning')
                break
            elif 12 <= hour <= 15:
                speak('Good Afternoon')
                break
            else:
                speak('Good Evening')
                break

        elif 'good afternoon' in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour <= 11:
                speak('Good Morning')
                break
            elif 12 <= hour <= 15:
                speak('Good Afternoon')
                break
            else:
                speak('Good Evening')
                break

        elif 'good evening' in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour <= 11:
                speak('Good Morning')
                break
            elif 12 <= hour <= 15:
                speak('Good Afternoon')
                break
            else:
                speak('Good Evening')
                break

        elif 'good night' in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour <= 11:
                speak('Good Morning')
                break
            elif 12 <= hour <= 15:
                speak('Good Afternoon')
                break
            else:
                speak('Good Evening')
                break


        elif 'weather' in query:
            try:
                # API_ID = "6bdc6*************ddb8"

                BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
                API_KEY = "6bdc6**************ddb8"
                speak('Tell Me The City Name.')
                CITY = takecommand().lower()
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
                break
            except:
                speak('Sorry, i did not understand the city name.')
                break

        # Alarm
        elif 'alarm' in query:
            alarmHour = int(input("Enter Hours: "))
            alarmMinute = int(input("Enter Minute: "))
            alarmAmPm = input("am / pm : ")
            if alarmAmPm == "pm":
                alarmHour += 12
            while True:
                if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
                    print("Wake Up")
                    playsound("C:\\Users\\neera\\PycharmProjects\\ERA\\SupermanRising.mp3")
                    break


        # Open Application
        elif 'open notepad' in query:
            OpenAndClose.OpenApps(query)
            break
        elif 'open microsoft word' in query:
            OpenAndClose.OpenApps(query)
            break
        elif 'open command prompt' in query:
            OpenAndClose.OpenApps(query)
            break
        elif 'open browser' in query:
            path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(path)
            speak('Opening Microsoft Edge Browser.')
            break
        elif 'open chrome' in query or "open cmd" in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            speak('Opening Chrome Browser.')
            break
        elif 'instagram' in query:
            webbrowser.open('www.instagram.com')
            speak('Opening Instagram.')
            break
        elif "start" in query:
            NameOfApp = query.replace("start ", "")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(NameOfApp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            break

        # Close Application.
        elif 'close notepad' in query:
            OpenAndClose.CloseApps(query)
            break
        elif 'close microsoft word' in query:
            OpenAndClose.CloseApps(query)
            break
        elif 'close command prompt' in query:
            OpenAndClose.CloseApps(query)
            break
        elif 'close browser' in query:
            os.system("TASKKILL /F /im msedge.exe")
            break
        elif 'close chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            speak('Close Chrome Browser')
            break

        # Screenshot.
        elif 'screenshot' in query:
            speak('Ok, What should i name that file')
            path = takecommand()
            path1name = path + ".png"
            path1 = "C:\\Image\\Screenshot\\" + path1name
            image = pyautogui.screenshot()
            image.save(path1)
            os.startfile("C:\\Image\\Screenshot")
            speak("Your Screenshot is here.")
            break

        # IP Address.
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP address is {ip}')
            break

        # Internet Speed
        elif 'internet speed' in query:
            FeaturesAndTasks.SpeedTest(query)
            break
        elif 'downloading speed' in query:
            FeaturesAndTasks.SpeedTest(query)
            break
        elif 'uploading speed' in query:
            FeaturesAndTasks.SpeedTest(query)
            break


        # Music
        elif 'music' in query:
            music_dir = 'C:\\Music\\My Favorite Songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak('Playing Music...')
            break


        # Wikipedia.
        elif 'wikipedia' in query:
            speak('Ok, What should i search on wikipedia')
            query = takecommand()
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=4)
            speak(results)
            print(results)
            break

        # Search on google with image.
        elif 'search' in query:
            import wikipedia as googleScrap
            query = query.replace('search', ' ')
            query = query.replace('What is ', ' ')
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query, 2)
                speak(result)
                break
            except:
                return "none"
                break

        # Google Search.
        elif 'google' in query:
            speak('What should i search on google.')
            cm = takecommand().lower()
            webbrowser.open(cm)
            break


        # How to make
        elif 'how to' in query:
            speak("Getting data from the internet")
            op = query.replace("friday", " ")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
            break


        # Website.
        elif 'website' in query:
            speak('Tell me the name of website.')
            name = takecommand().lower()
            website = 'https://www.' + name + '.com'
            webbrowser.open(website)
            speak('Opening...')
            break


        # YouTube Search
        elif 'youtube' in query:
            speak('What should i search on youtube.')
            cm = takecommand().lower()
            website = 'https://www.youtube.com/results?search_query=' + cm
            webbrowser.open(f'{website}')
            speak(cm)
            break


        # Reminder
        elif 'remind me' in query:
            remembermsg = query.replace("remind me", " ")
            speak('You tell me to remind you :'+remembermsg)
            remember = open('C:\\Users\\neera\\PycharmProjects\\AI Friday\\Data\\remind.text', 'w')
            remember.write(remembermsg)
            remember.close()
            break
        elif 'remember' in query:
            remember = open('C:\\Users\\neera\\PycharmProjects\\AI Friday\\Data\\remind.text', 'r')
            speak('You tell me to remind you:' + remember.read())
            break


        # Joke.
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            break

        # Automate Browser
        elif 'new tab' in query:
            press_and_release('ctrl + t')
            break
        elif 'close tab' in query:
            press_and_release('ctrl + w')
            break
        elif 'new window' in query:
            press_and_release('ctrl + n')
            break
        elif 'history' in query:
            press_and_release('ctrl + h')
            break
        elif 'download' in query:
            press_and_release('ctrl + j')
            break
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
            break
        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
            break
        elif 'switch tab' in query:
            Tab = query.replace('switch tab', '')
            tab = Tab.replace('to', '')
            num = tab
            kk = f'ctrl + {num}'
            press_and_release(kk)
            break


        elif 'open' in query:
            name = query.replace("open", "")
            Name = str(name)
            if 'youtube' in Name:
                webbrowser.open("https://www.youtube.com/")
                speak('Opening YouTube...')
                break
            elif 'instagram' in Name:
                webbrowser.open("https://www.instagram.com/")
                speak('Opening Instagram...')
                break
            else:
                string = "https://" + Name + ".com"
                string2 = string.replace(" ", "")
                string3 = string2.replace("  ", "")
                webbrowser.open(string3)
                speak('Opening' + name)
                break


        # Automate YouTube
        elif 'pause' in query:
            keyboard.press('space bar')
            break
        elif 'resume' in query:
            keyboard.press('space bar')
            break
        elif 'restart' in query:
            keyboard.press('0')
            break
        elif 'mute' in query:
            keyboard.press('m')
            break
        elif 'skip' in query:
            keyboard.press('l')
            break
        elif 'back' in query:
            keyboard.press('j')
            break
        elif 'full screen' in query:
            keyboard.press('f')
            break
        elif 'film screen' in query:
            keyboard.press('t')
            break
        elif 'theater mode' in query:
            keyboard.press('t')
            break
        elif 'mute' in query:
            keyboard.press('m')
            break
        elif 'unmute' in query:
            keyboard.press('m')
            break
        elif 'subtitle' in query:
            keyboard.press('c')
            break
        elif 'caption' in query:
            keyboard.press('c')
            break
        elif 'increase volume' in query:
            keyboard.press('up arrow')
            break
        elif 'decrease volume' in query:
            keyboard.press('down arrow')
            break
        elif 'increase speed' in query:
            press_and_release('shift + .')
            break
        elif 'search box' in query:
            keyboard.press('/')
            speak('what i search')
            search = takecommand()
            keyboard.write(search)
            keyboard.press('enter')
            break
        elif 'decrease speed' in query:
            press_and_release('shift + ,')
            break
        elif 'previous' in query:
            press_and_release('shift + p')
            break
        elif 'next' in query:
            press_and_release('shift + n')
            break


        # Automate Windows
        elif 'close app' in query:
            press_and_release('Alt + F4')
            break
        elif 'setting' in query:
            press_and_release('windows + i')
            break
        elif 'home screen' in query:
            press_and_release('windows + m')
            break
        elif 'minimize' in query:
            press_and_release('windows + m')
            break


        # NASA
        elif 'space news' in query:
            speak('Enter the date in the format of; year - month - date. For news extracting process')
            speak('Like: 2003-01-27 ')
            Date = input("Enter Date: ")
            # Date = Date.replace("  ", "")
            # Date = Date.replace(" ", "-")
            # Date = Date.replace("   ", "-")
            # Date = Date.replace("and", "-")
            # Date = Date.replace("and", "-")
            # Date = Date.replace(" and ", "-")
            FeaturesAndTasks.NasaNews(Date)
            break

        # Solar Body
        elif 'solar system' in query:
            speak('Tell me the object name in the solar system or the planets which you want to know.')
            Data = takecommand()
            Data = Data.replace(" ", "")
            Data = Data.replace("  ", "")
            Body = str(Data)
            FeaturesAndTasks.SolarBody(Body)
            break

        # Whatsapp automate
        elif 'whatsapp message' in query:
            query = query.replace("friday", "")
            query = query.replace("send", "")
            query = query.replace("whatsapp message", "")
            query = query.replace("to", "")
            name = query
            if 'vinita' in name:
                num = "6************"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_msg(num, mess)
                break
            elif 'papa' in name:
                num = "7************9"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_msg(num, mess)
                break
            elif 'neeraj' in name:
                num = "************"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_msg(num, mess)
                break
            elif 'ritesh' in name:
                num = "88**********8"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_msg(num, mess)
                break
            elif 'friend' in name:
                gro = "FzSPRlptL5DIDHSpphvNWy"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_grp(gro, mess)
                break
            elif 'data' in name:
                gro = "IBOQSwzg*******SS0h"
                speak(f"What's the message for {name}")
                mess = takecommand()
                FeaturesAndTasks.whatsapp_grp(gro, mess)
                break

        # Email
        elif 'email to neeraj' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'solanki@gmail.com'
                FeaturesAndTasks.sendEmail(to, content)
                speak('Email Send')
                break

            except Exception as e:
                print(e)
                speak('Email Not Send')
                break

        elif 'email to vinita' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'vinitasola@gmail.com'
                FeaturesAndTasks.sendEmail(to, content)
                speak('Email Send')
                break

            except Exception as e:
                print(e)
                speak('Email Not Send')
                break


# ................................................................................................................#
# ................................................................................................................#
# ................................................................................................................#
        # ...............Brain............... #
        # Question Answer.
        # elif "what is" in query or "how" in query or "where is" in query or "question" in query or "answer" in query:
        #     Reply = QuestionAnswer(query)
        #     speak(Reply)
        #     break
        #
        # else:
        #     Reply = ReplyBrain(query)
        #     speak(Reply)
        #     break
        #
        # break


        else:
            data = query
            data1 = TaskExecution(data)
            query = str(data1).lower()
            speak(query)
            break

        break

# TaskExe()
