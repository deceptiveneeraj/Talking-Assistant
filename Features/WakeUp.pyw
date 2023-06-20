import os
import speech_recognition as sr

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")

        except:
            return ""
        query = str(query).lower()
        print(query)
        return query

def WakeupDetected():
    query = Listen().lower()
    if 'wake up' in query:
        os.startfile("C:\\Users\\neera\\PycharmProjects\\AI Friday\\AI_Main.py")
        exit()
    else:
        pass

# while True:
#    WakeupDetected()
