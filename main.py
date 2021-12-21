from os import stat
from telegram.bot import Bot
from telegram.ext.commandhandler import CommandHandler
from telegram.user import User
from telegram.ext import Updater


updater = Updater(token='5000585937:AAEzHaMUeFyDYggKfKJ0XP0lAIF9GF_yrmc')


def start(update, context):
  print(update)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
