from Body.Listen import MicExecution
from Body.Speak import Speak
# from Body.Talk_Chrome import
# from Features.Alarm import Alarm
# from Features.ClapDetection import Tester
# from Main import Main_Task_Execution
import datetime
from Action import TaskExe
# from NN_ML_AI_NLP_DL.Main import Main_Task_Execution   # ...NN ML NLP AI DL

Speak('Hey, I Am Friday 5.0, Your personal virtual assistant.')
Speak('I am your latest innovation and best before all.')
Speak("Welcome Sir!")

# To Wish Me.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        Speak('Good Morning')
    elif 12 <= hour <= 15:
        Speak('Good Afternoon')
    else:
        Speak('Good Evening')


def Main():
    wishMe()
    # Speak('')
    while True:
        Data = MicExecution()
        Data = str(Data).lower()

#        ValueReturn = Main_Task_Execution(Data)
#        if ValueReturn == True:
#            pass

        if len(Data)<3:
            pass

        elif "friday" in Data:
            Data = Data.replace('friday', '')
            Data = Data.replace('Friday', '')
            Speak('Yes Sir...')
            TaskExe()
            print(Data)

        # elif "alina" in Data:
        #     Data = Data.replace('alina', '')
        #     Data = Data.replace('Alina', '')
        #     Speak('Yes Sir...')
        #     Main_Task_Execution()
        #     print(Data)


        # Exit Part.
        elif "break" in Data:
            Speak("I'll take a break if you'd like. Let me know when you're ready to continue...")
            break
        elif "close" in Data:
            Speak("I'll take a break if you'd like. Let me know when you're ready to continue...")
            break
        elif "shut up" in Data:
            Speak("Ok, i keep quit my mouth for now, i hope we can talk again soon ")
            break
        elif "be quiet" in Data:
            Speak("I will be quiet if that is what you wish.. ")
            break
        elif 'good night' in Data:
            Speak('Good night Sir!, have a sweet dream...')
            exit()
        elif 'exit' in Data:
            Speak('Thanks for using me , have a good day...')
            exit()
        elif 'stop' in Data:
            Speak('Thank you for talking with me. I hope we can talk again soon..')
            break
        elif 'off' in Data:
            Speak('Thank you for talking with me. I hope we can talk again soon..')
            break
        elif 'not now' in Data:
            Speak('Thanks for using me , have a good day...')
            exit()

Main()

# Clap Detection
"""def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("Clap Detected")
        print("")
        Main()
ClapDetect()"""

'''        
if __name__== "__main__":
    Main()
'''