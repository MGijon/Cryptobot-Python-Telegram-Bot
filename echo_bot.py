import telebot

TOKEN = '336549983:AAHyJp9-bLRm1N8vSXfy8XUwqOE_Tdi6tTI'
bot = telebot.TeleBot(TOKEN)

# Note: all handlers are tested in the order in which they were declared

@bot.message_handler(comands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "how are you doing?")

@bot.message_handler(func = lambda m : True)
def echo_all(message):
    bot.reply_to(message, message.text)

