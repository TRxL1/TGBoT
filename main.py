import telebot
bot = telebot.TeleBot('6373396991:AAGP1IvnXf33liIMm-MJThLh2kk6JR9_pMs')
@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name} </u></b>'
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')



bot.polling(none_stop=True)





