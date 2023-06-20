import pyttsx3
import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

# Speak
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate', 200)
def speak(text):
    print("   ")
    Assistant.say(text)
    print(f" {text}")
    print("   ")
    Assistant.runAndWait()


# Open Apps
def OpenApps(query):
    query = str(query).lower()

    if 'notepad' in query:
        path = 'C:\\Windows\\System32\\notepad.exe'
        os.startfile(path)
        speak('Opening Notepad.')

    elif 'microsoft word' in query:
        path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word'
        os.startfile(path)
        speak('Opening MS Word')

    elif 'command prompt' in query:
        os.system('start cmd')
        speak('Opening Command Prompt.')

# Close Application.
def CloseApps(query):
    query = str(query).lower()

    if 'notepad' in query:
        os.system("TASKKILL /F /im notepad.exe")

    elif 'microsoft word' in query:
        os.system("TASKKILL /F /im WINWORD.EXE")

    elif 'command prompt' in query:
        os.system("TASKKILL /F /im cmd.exe")
