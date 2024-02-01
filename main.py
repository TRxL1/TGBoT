print("Hello,World!")
read_input = input()
print(read_input)
import telebot
bot = telebot.TeleBot('6373396991:AAGP1IvnXf33liIMm-MJThLh2kk6JR9_pMs')
@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет<b>', parse_mode='html')



bot.polling(none_stop=True)



