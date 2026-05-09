import telebot
import random
from telebot.types import Message

bot = telebot.TeleBot(token='8665934273:AAFwfGsZfJ7FIdXoYYkbgBAi0dq_owcPzO0')

#     НАЧАЛЬНЫЙ ТЕКСТ ПРИ ЗАПУСКЕ БОТА
@bot.message_handler(commands=['start'])
def cmd_start(message: Message) -> None:
        user_name = message.from_user.username

        text = {
            f"Привет {user_name}! \n\n"
            f"Я бот для генерации рандомных приколов. \n\n"
            f"/coin - подбросить монетку\n"
            f"/\n"
            f"/\n"
            f"/\n"
            f"Попробуй прямо сейчас"
        }

        bot.reply_to(message = message, text=text)


if __name__ == '__main__':
    print("ГАЗ!, все зепустилось")
    bot.infinity_polling()
