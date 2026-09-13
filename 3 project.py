import telebot
import time
import threading

token = '8912564239:AAGxZPgLMwxgV-AUShOgPZqap5GnJwwxhCU'

bot = telebot.TeleBot(token)

hum = {}

def ensure_user(user_id):
    if user_id not in hum:
        hum[user_id] = {
            "goal": 2000,
            "item": 0,
            "run": False,
        }
    return hum[user_id]

@bot.message_handler(commands=['start'])
def start_message(message):
    ensure_user(message.from_user.id)
    bot.send_message(message.chat.id,'Привет! Я бот для напоминания выполнять нормы выпитой воды в течении дня.Чтобы запустить и выпивать воду в такое время какое хочешь,используй команду /setremandier,и введи количество часов,а чтобы давать отчет о выпитой воды,используй команду /drank,а чтобы узнать сколько еще воды нужно выпить,используй команду /status,а чтобы остановить таймер,используй команду /stop')
    
 
@bot.message_handler(commands=['setremandier'])
def button_message(message):
    try:
        bot.send_message(message.chat.id,'Насколько запустить таймер? Введите количество часов:')
        bot.register_next_step_handler(message, get_reminder_time)
    except ValueError:
        bot.send_message(message.chat.id,'Пожалуйста, введите число!')
    

@bot.message_handler(commands=['drank'])
def drank_message(message):
    ensure_user(message.from_user.id)
    bot.send_message(message.chat.id, 'Так сколько же ты выпил воды (в мл)?')
    bot.register_next_step_handler(message, process_drank_input)

@bot.message_handler(commands=['status'])
def status_message(message):
    user = ensure_user(message.from_user.id)
    fff = user["goal"] - user["item"]
    bot.send_message(message.chat.id, f'Тебе осталось выпить {fff} мл воды.')
    if fff <= 0:
        bot.send_message(message.chat.id,f'Поздравляю! Ты выполнил дневную норму!Надеюсь что завтра начнем с начала,пока!')

def reminder_loop(chat_id, remi, user_id):
    user = ensure_user(user_id)

    while user["run"]:
        time.sleep(remi)

        if user["run"]:
            bot.send_message(chat_id, 'Прошло заданное время! Время выпить воду!')

def get_reminder_time(message):
    try:
        reminder = int(message.text)
        bot.send_message(message.chat.id, f'Я запустил таймер на {reminder} час!')

        remi = reminder * 60 * 60
        user = ensure_user(message.from_user.id)
        user["run"] = True

        thread = threading.Thread(
            target=reminder_loop,
            args=(message.chat.id, remi, message.from_user.id),
            daemon=True
        )
        thread.start()

    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число!')

def process_drank_input(message):
    try:
        drank_amount = int(message.text)
        user = ensure_user(message.from_user.id)
        user["item"] += drank_amount
        bot.send_message(message.chat.id, f'Отлично! Я запомнил что ты выпил {drank_amount} мл воды!')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число!')

@bot.message_handler(commands=['stop'])
def stop_reminder(message):
    user = ensure_user(message.from_user.id)
    user["run"] = False
    bot.send_message(message.chat.id, 'Таймер остановлен!')

bot.infinity_polling()