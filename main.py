import telebot
import webbrowser

bot = telebot.TeleBot('8475126236:AAGSI-_Q5QOm0yjwMUbxAaJH8ddpS4nB3nw')
# начало работы с ботом
@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B9%D0%BC%D0%B0%D1%80')
#Это (webbrowser.open) команда с помощью которой можно открыть сайт в браузере, она находится в библиотеки webbrowser
@bot.message_handler(commands=['start'])
# после start можно написать другую программу чрез запятую в кавычках, тоже выведет сообщение
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
# действие после команды
# если пишем после запятой message, то получаем всю информацию по сообщению, если же пишем к примеру message.first_name, то только определенную.
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Тоби </b> <em><u>ПИЗДА</u></em>',parse_mode='html')
# Если введено parse_mod=html то можно с помощью html форматировать данный текст под свое усмотрение к примеру сделать его жирным.
@bot.message_handler(content_types=['photo','audio'])
def get_photo(message):
    bot.reply_to(message, 'Какое красивое фото')
@bot.message_handler()
# теперь можно работать с любыми сообщениями пользователя, независимо от самого текста
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
# этот метод лучше располагать в самом конце,т.к. он реагирует на любой текст, который мы ввели, а значит не дает такому же методу с определенным месаджем сработать
import logging
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(func=lambda m: True, content_types=['text','photo','audio','voice','document','video','sticker'])
def debug_echo(message):
    print("Got:", message.chat.type, message.content_type, getattr(message, 'text', None))
import time, requests
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except requests.exceptions.ReadTimeout:
        time.sleep(2)
        continue
    except Exception:
        time.sleep(5)


# это обязательно пишется после всего отсального кода
# бот работает постоянно
#можно написать bot.infinity_polling() произойде тоже самое
