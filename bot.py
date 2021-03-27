import logging
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from telegram.utils.request import Request
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log')

def start_bot(update: Update, context: CallbackContext):
	# print(update)
	first_name = format(update.message.chat.first_name)
	hello_text = """Привет %s!
Я простой бот Жека и я повторяю за тобой всё!
	""" % (first_name)

	update.message.reply_text(hello_text)


def chat(update: Update, context: CallbackContext):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)


def main():

	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()


if __name__ == "__main__":
	logging.info('Bot started')
	main()