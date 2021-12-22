
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.update import Update
from telegram.ext.filters import Filters
import settings
import requests


updater = Updater(token = settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
  update.message.reply_text\
    ("Assalomu alaykum Wikipediya ma'lumot qidiruv botiga hush kelibsiz!"
      "/search ........")

def search(update: Update, context: CallbackContext):
  args = context.args

  if len(args) == 0:
    update.message.reply_text\
    ("/search ........")
  else:
    searchText = ' '.join(args)
    response = requests.get('https://uz.wikipedia.org/w/api.php', {
      'action': 'opensearch',
      'search': searchText,  
      'limit': 1,
      'namespace': 0,
      'format': 'json',
    })
    result = response.json()
    link = result[3]
  
    if len(link):
      update.message.reply_text('Havola topildi marhamant: 👉' + link[0])
    else:
      update.message.reply_text('🙅 Afsus havola topilmadi Qaytadan urinib ko`ring')
    

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start)) 


updater.start_polling()
updater.idle()
