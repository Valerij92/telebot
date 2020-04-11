import telebot

bot = telebot.TeleBot('758839187:AAEgXFt5DfKnUrUuQg74t3kSdN1CFt1lBjE')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Здарова {message.from_user.first_name} {message.from_user.last_name}</b>!\nЧто тебе надо?"
    bot.send_message(message.chat.id.send_mess, parse_mode='html')


bot.polling(none_stop= True)