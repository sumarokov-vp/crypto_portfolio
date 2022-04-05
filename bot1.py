import telebot

bot = telebot.TeleBot('640519344:AAEdRL3ToVuvCXJr4yumA4GzCrYek7ewuVU')

@bot.message_handler(commands=['start'])
def start_handler(message: telebot.types.Message):
    if message.from_user.first_name is None and message.from_user.last_name is not None:
        name = message.from_user.last_name
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        name = message.from_user.first_name
    elif message.from_user.first_name is not None and message.from_user.last_name is not None:
        name = message.from_user.first_name + ' ' + message.from_user.last_name
    else: name = ''
    bot.send_message(chat_id= message.chat.id, text= 'OK I see you')

bot.polling()
