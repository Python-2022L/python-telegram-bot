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

def start(update: Update, context: CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   first_name = update.message.chat.first_name
   bot.sendMessage(chat_id, f'Hello, {first_name}')

def echo(update: Update, context:CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   text = update.message.text
   bot.sendMessage(chat_id, text)

def video(update, context):
   print("VIDEO")

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.video, video))

updater.start_polling()
updater.idle()
