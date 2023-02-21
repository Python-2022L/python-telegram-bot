from telegram.ext import (
   Updater, 
   CommandHandler, 
   CallbackContext, 
   MessageHandler, 
   Filters
   )
from telegram import Update
import os

TOKEN=os.environ["TOKEN"]

def hello(update: Update, context: CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   first_name = update.message.chat.first_name
   bot.sendMessage(chat_id, f'Hello, {first_name}')

def echo(update: Update, context:CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   text = update.message.text
   bot.sendMessage(chat_id, text)

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
