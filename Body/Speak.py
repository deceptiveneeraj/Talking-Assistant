import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    # print(voices)
    # print(voices[4].id)
    engine.setProperty('rate', 200)
    print("")
    print(f"AI : {Text}.")
    print("")
    engine.say(Text)
    # engine.save_to_file('')
    engine.runAndWait()

# Speak("Hey, I Am Friday 5.0, Your personal virtual assistant.")
