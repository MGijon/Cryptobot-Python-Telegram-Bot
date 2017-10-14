ALPH_LENG = 26

import telebot

TOKEN = '336549983:AAHyJp9-bLRm1N8vSXfy8XUwqOE_Tdi6tTI'
bot = telebot.TeleBot(TOKEN)

# getMe
#user = bot.get_me()

# ------------------------------------------------------------
# COMMANDS:
# ------------------------------------------------------------

##  HELP

@bot.message_handler(commands = ['help'])
def random_name(message):
    bot.reply_to(message, 'Cammon, you only need to work harder men!')


## START

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, instrucciones de uso a añadir aquí')


## ROT 13

@bot.message_handler(commands = ['rot13'])
def root(message):
    message.text = message.text[len('rot13') + 1 : ]
    message.text = algorithmROT13(message.text)
    bot.reply_to(message, message.text)

## CESAR ENCRYPT

@bot.message_handler(commands = ['cesare'])
def cesar(message):
    '''
    Cesar para encriptar. formato cesar 00 mensaje
    :param message:
    :return:
    '''
    message.text = message.text[len('cesare') + 1: ] # con esto pillo hasta
    key =int( message.text[1:3])                        # obtengo la clave
    message.text = message.text[3:]               # obtengo el mensaje a encyptar
    message.text = algorithmCesar(message.text, key)
    bot.reply_to(message, message.text)

## CESAR DECRYPT

@bot.message_handler(commands = ['cesard'])
def cesar(message):
    '''
    Cesar para desencryptar. formato cesar 00 mensaje
    :param message:
    :return:
    '''
    message.text = message.text[len('cesard') + 1: ] # con esto pillo hasta
    key = - int( message.text[1:3])                        # obtengo la clave
    message.text = message.text[3:]               # obtengo el mensaje a encyptar
    message.text = algorithmCesar(message.text, key)
    bot.reply_to(message, message.text)


# ------------------------------------------------------------
# ENCYPT / DECRYPT ALGORITHMS:
# ------------------------------------------------------------

## ROT 13

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


## CESAR

def algorithmCesar(mIn, key):

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


# ------------------------------------------------------------
# OTHERS:
# ------------------------------------------------------------

bot.polling(none_stop = False, interval = 0, timeout = 20)




