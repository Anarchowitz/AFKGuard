#v:1.0.0
import telebot
import time, os
import pyautogui
#НАСТРОЙКИ
TOKEN = "в этих ковычках заместо слов токен" # <-- Сюда токен из созданого бота @botfather телеграм (НЕ УБИРАЙТЕ КОВЫЧКИ - ВНУТРИ КОВЫЧЕК ДОЛЖЕН БЫТЬ ТОКЕН)
YOUR_CHAT_ID = "в этих ковычках заместо слов чат айди" # <-- Сюда чат айди (узнать можно в боте - @chatIDrobot в тг или другим способом.) (НЕ УБИРАЙТЕ КОВЫЧКИ - ВНУТРИ КОВЫЧЕК ДОЛЖЕН БЫТЬ ЧАТ АЙДИ)
bot = telebot.TeleBot(TOKEN, parse_mode=None)
#--------------------------------------------------------------------------------------------------------------
step = 0
k = 0
z = 0
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id == int(YOUR_CHAT_ID):
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = telebot.types.KeyboardButton('[📸] Скриншот 60 раз в 1 мин (Default mode)')
        button1 = telebot.types.KeyboardButton('[📸] Скриншот(Custom mode)')
        keyboard.add(button1,button2)
        step = 0
        bot.send_message(message.chat.id, "👋 Привествую юзер AFKGuard`а! Используйте кнопки меню в телеграмме, чтобы выбрать режим.")
        bot.send_message(message.chat.id, "[❗] - Кнопки не будут работать если цикл уже начался, после завершения - все будет доступно (перезапуском /start)", reply_markup=keyboard)
        print('Показал меню\n')
    else:
        print('[❗ ]Кто-то другой попытался использовать бота [❗ ]\n')
        bot.send_message(message.chat.id, "[ ❌ ] - Acces denied")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.id == int(YOUR_CHAT_ID):
        global step, k, z
        if step == 0:
            if message.text == "[📸] Скриншот 60 раз в 1 мин":
                print('Начинаю делать циклы.\n')
                for i in range(60):
                    image = pyautogui.screenshot()
                    image.save("screenshot.png")
                    bot.send_photo(message.chat.id, open("screenshot.png", "rb"))
                    print(f'Сделал скриншот, ожидаю таймер. Это был {i+1} из 60 скриншотов')
                    time.sleep(60)
                bot.send_message(message.chat.id, f'[✔️] Успешно. Цикл успешно выполнен!')
                step = 0
            elif message.text == "[📸] Скриншот(Custom mode)":
                bot.send_message(message.chat.id, "[⏳] Введите количество скриншотов : ")
                step = 1
        elif step == 1:
            if message.text.isdigit() == True:
                k = int(message.text)
                bot.send_message(message.chat.id, '[🔢] Задержка перед скриншотами (в секундах): ')
                step += 1
            else:
                bot.send_message(message.chat.id, '[✖️] - Введите число.')
        elif step == 2:
            if message.text.isdigit() == True:
                z = int(message.text)
                step += 1
                bot.send_message(message.chat.id, f'[✔️] Успешно. Количество = {k}, Таймер = {z}')
                print('Начинаю делать циклы.\n')
                for i in range(k):
                    image = pyautogui.screenshot()
                    image.save("screenshot.png")
                    bot.send_photo(message.chat.id, open("screenshot.png", "rb"))
                    print(f'Сделал скриншот, ожидаю таймер. Это был {i+1} из {k} скриншотов')
                    time.sleep(z)
                bot.send_message(message.chat.id, f'[✔️] Успешно. Цикл успешно выполнен!')
                print('\n Цикл завершен.')
                step = 0
            else:
                bot.send_message(message.chat.id, '[✖️] - Введите число.')
if __name__ == '__main__':
    os.system('cls & title AFKGuard')
    print("""
AFKGUARD - Загружен!
Приятного использования.
--------------------
          Логи бота:
        """)
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)
#maded by anarch
#dont copy this shit code please
