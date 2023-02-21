from telegram.ext import (
   Updater, 
   CommandHandler, 
   CallbackContext, 
   MessageHandler, 
   Filters
   )
from telegram import (
   Update,
   ReplyKeyboardMarkup,
   KeyboardButton
   )
import os

TOKEN=os.environ["TOKEN"]

def start(update: Update, context: CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   first_name = update.message.chat.first_name

   button1 = KeyboardButton(text='DOG')
   button2 = KeyboardButton(text="CAT")

   reply_markup = ReplyKeyboardMarkup([[button1, button2]], resize_keyboard=True)

   bot.sendMessage(chat_id, f'Hello, {first_name}', reply_markup=reply_markup)

def echo(update: Update, context:CallbackContext):
   bot = context.bot
   chat_id = update.message.chat.id
   text = update.message.text
   bot.sendMessage(chat_id, text)


updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
