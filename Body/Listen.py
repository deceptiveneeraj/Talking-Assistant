from googletrans import Translator                              # pip install googletrans
import speech_recognition as sr                                 # pip install SpeechRecognition
#  From Archived: Unofficial Windows Binaries for Python Extension Packages " https://www.lfd.uci.edu/~gohlke/pythonlibs/ "
# pip install .\PyAudio-0.2.11-cp311-cp311-win_amd64.whl


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
#       audio = r.listen(source)

        try:
            print("Recognizing...")
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

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

# while True:
#    Data = MicExecution()
#    Data = str(Data).lower()
