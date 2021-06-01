from time import sleep
import pyautogui
import telebot
import os
from os.path import join, dirname
from dotenv import load_dotenv

env = join(dirname(__file__), ".env")
load_dotenv(env)
print(env)

token = os.environ.get("TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id, 'Queue'.format(chat_id))

    while True:
        if check_screen():
            print('Match accepted.')
            sendMsg(chat_id)
            sleep(6)
            break


def sendMsg(chat_id):
    bot.send_message(chat_id, 'Match accepted.')


def click(x, y):
    pyautogui.click(x, y)


def check_screen():
    button = pyautogui.locateOnScreen('en.png', confidence=0.7)
    buttonPt = pyautogui.locateOnScreen('pt.png', confidence=0.7)

    if button != None:
        click(button.left, button.top)
        return True

    if buttonPt != None:
        click(buttonPt.left, buttonPt.top)
        return True

    return False

bot.polling()
