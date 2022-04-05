import telebot
import db

bot = telebot.TeleBot(db.get_setting('bot'))

@bot.message_handler(commands=['start'])
def start_handler(message: telebot.types.Message):
    if message.from_user.first_name is None and message.from_user.last_name is not None:
        name = message.from_user.last_name
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        name = message.from_user.first_name
    elif message.from_user.first_name is not None and message.from_user.last_name is not None:
        name = message.from_user.first_name + ' ' + message.from_user.last_name
    else: name = ''
    id = db.create_user(name= name, chat_id= message.chat.id)
    bot.send_message(chat_id= message.chat.id, text= str(id))

bot.polling()
