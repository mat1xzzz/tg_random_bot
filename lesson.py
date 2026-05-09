import telebot
import random
from telebot.types import Message

bot = telebot.TeleBot(token='8665934273:AAFwfGsZfJ7FIdXoYYkbgBAi0dq_owcPzO0')


#------------------------------------------------
#     НАЧАЛЬНЫЙ ТЕКСТ ПРИ ЗАПУСКЕ БОТА
#------------------------------------------------

@bot.message_handler(commands=['start'])
def cmd_start(message: Message) -> None:
        user_name = message.from_user.username

        text = (
            f"Привет {user_name}! \n\n"
            f"Я бот для генерации рандомных приколов. \n\n"
            f"/coin - подбросить монетку\n"
            f"/dice - подбросить кубик\n"
            f"/\n"
            f"/\n"
            f"Все запустилось, ГАЗ!"
        )

        bot.reply_to(message=message, text=text)


#------------------------------------------------
#           ПОДБРОС МОНЕТЫ
#------------------------------------------------

@bot.message_handler(commands=['coin'])
def cmd_coin(message: Message) -> None:
    coin_result = random.choice([f"ОРЕЛ!", "РЕШКА!"])
    bot.reply_to(message = message, text = coin_result)


#------------------------------------------------
#                ПОДБРОС КУБИКА
#------------------------------------------------
@bot.message_handler(commands=['dice'])
def cmd_dice(message: Message) -> None:
    # 1 ⚀ 2 ⚂ 3 ⚁ 4 ⚃ 5 ⚄ 6 ⚅
    number = random.randint(1, 6)
    dice_emoji = {
        1: "⚀",
        2: "⚁" ,
        3: "⚁",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }

    dice_result = f"Выпало: {dice_emoji[number]} ({number})"
    bot.reply_to(message = message, text = dice_result)


#------------------------------------------------
#          ГЕНЕРАТОР ПАРОЛЕЙ
#------------------------------------------------

@bot.message_handler(commands=['help'])
def cmd_password(message: Message) -> None:
    password = random


if __name__ == '__main__':
    print("ГАЗ!, все зепустилось")
    bot.infinity_polling()
