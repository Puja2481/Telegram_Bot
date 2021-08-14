# Telegram_Bot
This is the telegram bot using python

## README
```Note – This code only acts as a source code. All the credentials are hidden.```

### TELEGRAM BOT using Python 
 
Let’s understand what bot is.
Bots are third party applications that run inside telegram. Users can interact with bot by sending messages, commands, and inline requests.

Steps to make telegram bot:
Download and install telegram for desktop
### Register a telegram bot. 
Go to telegram desktop -> search bot father -> write the following commands
/start (to start)
/new bot (to register a new bot)
After that give your bot a name and username. (Here we are creating news bot )
Let’s say name = newsbot and username = news_2481 then you will get a token (token helps you to connect with the bot).

### Setting up the Project
        1.	Setup a Python Virtual Environment
        A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them.
        •	Create a project folder.
        •	Run the following command to create a new virtual environment inside your project folder:
        Python -m venv myvenv
        After running above command, a folder named myvenv will get created in your project folder.
        •	Activate the virtual environment by running the following command:
        •	For ubuntu and mac users:
        source myvenv/bin/activate
        •	For window users:
        myvenv\Scripts\activate
        
        
        2.	Install required Python Packages
        •	Python-telegram-bot
        pip install python-telegram-bot
        
        
        3.	Import some libraries
        import logging
        from flask import Flask, request
        from telegram.ext import Updater, Filters, CommandHandler, MessageHandler,Dispatcher
        from telegram import Bot, Update, ReplyKeyboardMarkup
        from utils import get_reply, fetch_news, topics_keyboard
        

### Polling Program  

###     Creating an Echo bot

        1.	Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - 
        %(message)s', level=logging.INFO)   
        # basic configration - take time,name, level, and giving message    
        logger = logging.getLogger(__name__)        # logger object

        2.	Create updater
        updater = Updater(TOKEN)    # updater will keep polling

        3.	Create Dispatcher
        dp = updater.dispatcher # creating a dispatcher object - handles the update

        4.	Add handler
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("news", news))
        dp.add_handler(MessageHandler(Filters.text, reply_text))   
        #if the user sends text
        dp.add_handler(MessageHandler(Filters.sticker, sticker))  
        #if the user sends sticker
        dp.add_error_handler(error)

        5.	Start polling and wait for any signal to end the program
        updater.start_polling()
        updater.idle()

### Setting up a webhook for a telegram bot
 
          Ports currently supported for the webhooks are 443, AP, 88, 8443.
          //Callback URL to telegram and we tell them that the server will keep running and it will accept the request from the user.
          Telegram server is responsible and tell us we got a request.
          Setting up a server
          1.	install flask
          pip install flask
          2.	set up webhook
          # create telegram bot object
          bot =  Bot(TOKEN)

          #set webhook for telegram bot

          bot.set_webhook("Enter Your Server Link" + TOKEN) # need a web url not a local url

          3.	create view two handle webhooks.
          # creating a view to handle webhooks
          @app.route(f'/{TOKEN}', methods=['GET', "POST"])
          def webhook():
              """Webhook view which recieves updates from telegram"""
              #create update object from  json-format request data
              update = Update.de_json(request.get_json(), bot)
              #process update
              dp.process_update(update)
              return "ok"

          server program
          Generate a public URL for webhook using ngrok.io.
          ngrok is a free tool that allows us to tunnel from public URL to our application running locally.
          1.	Download ngrok.
          2.	Unzip it.
          3.	Run ngrok from command line (from the location where executable installed)
          ./ngrok http 8443
          4.	Copy the HTTP is forwarding URL.

###  Train the boat using dialogflow
          Introduction to dialogflow
          Dialogflow is a kind of conversational engine which is a project maintain by Google itself.
          It helps you to create agent and that agent will be taught a bit about the different kind of intense and the entities that we have in a particular conversation
          Intents is what the user wants for example -to get news.
          Entities is objects around which we want to make a conversation. For example- location, language, topic.
          1.	Log in into dialogflow console.
          2.	Creator new agent or import a pre-built agent.
          3.	From settings page of agent, open the service account of your project indie Google Cloud Console.
          After these steps add some Custom keyboard in your telegram bot and then finally deploy flask app for telegram bot on Heroku.

