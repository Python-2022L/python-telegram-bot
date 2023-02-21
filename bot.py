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

   button1 = KeyboardButton(text='Contact')
   button2 = KeyboardButton(text="Category")

   reply_markup = ReplyKeyboardMarkup([[button1, button2]], resize_keyboard=True)

   bot.sendMessage(chat_id, f'Hello, {first_name}', reply_markup=reply_markup)

def contact(update, context):
   bot = context.bot
   chat_id = update.message.chat.id

   bot.sendMessage(chat_id, "+998992344334")

def category(update, context):
   bot = context.bot
   chat_id = update.message.chat.id

   button1 = KeyboardButton(text="G'ijduvon")
   button2 = KeyboardButton(text="Kogon")

   reply_markup = ReplyKeyboardMarkup([[button1, button2]], resize_keyboard=True)
   bot.sendMessage(chat_id, f'Qayerga ketasiz?', reply_markup=reply_markup)

def echo(update, context):
   bot = context.bot
   chat_id = update.message.chat.id
   text = update.message.text

   bot.sendMessage(chat_id, text)


updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Contact"), contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Category"), category))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
