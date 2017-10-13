ALPH_LENG = 26

import telebot

bot = telebot.TeleBot('336549983:AAHyJp9-bLRm1N8vSXfy8XUwqOE_Tdi6tTI')

# getMe
user = bot.get_me()


# recoge el comando '/start' y devuelve lo propio
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')

# recoge el comando '/help' y devuelve lo propio
@bot.message_handler(commands = ['help'])
def random_name(message):
    bot.reply_to(message, 'What kind of help do you need?')

# nuestro filtro replica cualquier otro mensaje que le pasemos
@bot.message_handler(func = lambda m : True)
def echo_all(message):
    message.text = algorithmROT13(message.text)
    bot.reply_to(message, message.text)


def algorithmROT13(mIn):
    mOut = ''
    for l in mIn:
        if l.isalpha():                 # letters

            s = ord(l)
            s += 13
            if l.isupper():
                if s > ord('Z'):
                    s -= ALPH_LENG
                elif s < ord('A'):
                    s += ALPH_LENG
            elif l.islower():
                if s > ord('z'):
                    s -= ALPH_LENG
                elif s < ord('a'):
                    s += ALPH_LENG

            mOut += chr(s)
        else:                           # other simbols

            mOut += l

    return mOut



bot.polling(none_stop = False, interval = 0, timeout = 20)