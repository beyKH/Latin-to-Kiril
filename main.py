from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '1489182860:AAFaJwNSPdr4-eRxeaW3Ll1dXi93hkw_lbs'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, Xush kelibsiz!\n mant kiring: ")

bot.polling()


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
	bot.reply_to(message, answer)

# text = input("Please enter text: ")
# if text.isascii() == True:
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
