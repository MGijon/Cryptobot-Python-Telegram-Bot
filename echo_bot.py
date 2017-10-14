ALPH_LENG = 26

import telebot

TOKEN = '336549983:AAHyJp9-bLRm1N8vSXfy8XUwqOE_Tdi6tTI'
bot = telebot.TeleBot(TOKEN)

# getMe
#user = bot.get_me()

OPCION = ''   # clase de encriptación que utilizaremos

# ------------------------------------------------------------
# HELP:
# ------------------------------------------------------------


# recoge el comando '/help' y devuelve lo propio
@bot.message_handler(commands = ['help'])
def random_name(message):
    bot.reply_to(message, 'Cammon, you only need to work harder men!')


# recoge el comando '/start' y devuelve lo propio
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, instrucciones de uso a añadir aquí')


# ------------------------------------------------------------
# RESPONSES:
# ------------------------------------------------------------


temp = True
@bot.message_handler(fun = temp)
def respuesta1(message):
    temp = False
    OPCION = message.text
    message.text = 'You have choosen ' + OPCION
    bot.reply_to(message, message.text)

'''
@bot.message_handler(func = lambda m : True)
def echo_all(message):
    message.text = algorithmROT13(message.text)
    bot.reply_to(message, message.text)
'''



# ------------------------------------------------------------
# ENCYPT / DECRYPT:
# ------------------------------------------------------------

# ROT 13



def algorithmROT13(mIn):
    mOut = ''
    for l in mIn:
        if l.isalpha():                 #

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
        else:

            mOut += l

    return mOut



# ------------------------------------------------------------
# OTHERS:
# ------------------------------------------------------------

bot.polling(none_stop = False, interval = 0, timeout = 20)



'''

def algorithmCesar(mIn, key, mode):

    if mode in 'decrypt d'.split():
        key = - key

    mOut = ''
    for l in mIn:
        if l.isalpha():                 # letters

            s = ord(l)
            s += key

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



'''