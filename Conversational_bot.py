import logging
from flask import Flask, request
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler,Dispatcher
from telegram import Bot, Update, ReplyKeyboardMarkup
from utils import get_reply, fetch_news, topics_keyboard

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',     #take time,level,name
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "Enter Your Token ID"   #token id


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route(f'/{TOKEN}', methods=['GET', "POST"])
def webhook():
    """Webhook view which recieves updates from telegram"""
    #create update object from  json-format request data
    update = Upadte.de_json(request.get_json(), bot)
    #process update
    dp.process_update(update)
    return "ok"

def start(bot,update):
    name  = update.message.from_user.first_name  #first name of the user messaging
    reply = "Hi!! {}".format(name)
    bot.send_message(chat_id = update.message.chat_id, text = reply)      #sending message

def help(bot,update):
    reply = "This is the help chat. How can I help You?"
    bot.send_message(chat_id = update.message.chat_id, text = reply)  #sending message

def news(bot, update):
    bot.send_message(chat_id= update.message.chat_id,text="Choose a category",
        reply_markup= ReplyKeyboardMarkup(keyboard= topics_keyboard, one_time_keyboard = True))



'''def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = reply)'''

def reply_text(bot,update):
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "get_news":
        articles = fetch_news(reply)
        for article in articles:
        #reply_text = "Ok! I will show you news with {}".format(reply)
        bot.send_message(chat_id=update.message.chat_id, text= article['link'])
    else:
        bot.send_message(chat_id=update.message.chat_id, text= reply)

   # bot.send_message(chat_id = update.message.chat_id, text = reply)

def sticker(bot,update):
    reply = update.message.sticker.file_id
    bot.send_sticker(chat_id = update.message.chat_id, sticker = reply)

def error(bot,update):
    logger.error("Sorry!! Update {} caused error {}".format(update,update.error))


    #updater.start_polling()
    #logger.info("Started...")
    #updater.idle()



if __name__=="__main__":
    bot =  Bot(TOKEN)
    bot.set_webhook("Enter Your Server Link" + TOKEN)

    dp = Dispatcher(bot, None)

    #updater = Updater(TOKEN)  #take the updates
    #dp = updater.dispatcher   #handle the updates

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(MessageHandler(Filters.text, reply_text))   #if the user sends text
    dp.add_handler(MessageHandler(Filters.sticker, sticker))  #if the user sends sticker
    dp.add_error_handler(error)
    app.run(port= 8443)