
import random
import telebot
from telebot import types

token = "5574756847:AAEU7jc0Yk96VgBMYeu3UmzmC8aCMh36fso"

bot = telebot.TeleBot(token)


markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('Вычисления')
itembtn2 = types.KeyboardButton('Угадай Число')

def getRndNum():
    return random.randint(1, 1001)
rndNum = getRndNum()

count_RndNum = 0

def setCurrentState(state):
    with open("currentstate.txt", "w", encoding="utf-8") as f:
        print(state)
        f.write(str(state))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def hello_user(message):
    if message.text == 'Вычисления':
        bot.reply_to(message, 'Калькулятор. Введите выражение')
        setCurrentState(1)

    elif message.text == 'Угадай Число':
        bot.reply_to(
            message, 'Введи от 1 до 100 и начни угадывать')
        setCurrentState(2)
    else:
        with open("currentstate.txt", "r", encoding="utf-8") as f:
            currentState = f.read()

        print(currentState, type(currentState), len(currentState))

        if currentState == "1":
            print(message.text)
            bot.reply_to(message, f'ответ = {eval(message.text)}')

        elif currentState == "2":
            global rndNum
            global count_RndNum
            if int(message.text) != rndNum:
                bot.reply_to(message, f'ответ = {rndNum}, а ты прислал {message.text}')
                count_RndNum = count_RndNum + 1
            else:
                bot.reply_to(message, f'ответ = {rndNum}, ура, ты победил за {count_RndNum} раз')
                
                rndNum = getRndNum()
                count_RndNum = 0
                
        else:
            bot.reply_to(message, 'что-то пошло не так')
                
                
bot.infinity_polling()