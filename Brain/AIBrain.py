# Api Key
# fileopen = open("C:\\Users\\neera\\PycharmProjects\\AI Friday\\Data\\API.txt", "r")
fileopen = open("C:\\Users\\neera\\PycharmProjects\\ADatabase\\API\\OpenApi.txt", "r")
API = fileopen.read()
fileopen.close()
# print(API)

# Importing
import openai                                   # pip install openai
from dotenv import load_dotenv                  # pip install python-dotenv

# Code
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question, chat_log = None):
    FileLog = open(f"C:\\Users\\neera\\PycharmProjects\\AI Friday\\Brain\\Brain.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\n AI :'
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nAI : {answer}"
    FileLog = open(f"C:\\Users\\neera\\PycharmProjects\\AI Friday\\Brain\\Brain.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

# print(ReplyBrain("What is my name?"))