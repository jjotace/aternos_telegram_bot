#Libraries
import config
import telebot  #pip install pyTelegramBotAPI
import threading 
import python_aternos #pip install python-aternos
from python_aternos import Client

#Telegram bot token
bot_token = config.TELEGRAM_TOKEN 

mybot = telebot.TeleBot(bot_token)


#respond to command /start
@mybot.message_handler(commands = ["start"])
def cmd_start(message):
    try :
        s.start() #with this we start the server
        mybot.send_message(config.TELEGRAM_GROUP_ID, config.START_SERVER_MESSAGE)
    except python_aternos.aterrors.ServerError:
        mybot.send_message(config.TELEGRAM_GROUP_ID, config.SERVER_START_ERROR_MESSAGE) 


#respond to command /stop
@mybot.message_handler(commands = ["stop"])
def cmd_stop(message):
    s.stop()
    mybot.send_message(config.TELEGRAM_GROUP_ID, config.STOP_SERVER_MESSAGE)


#respond to command /address
@mybot.message_handler(commands = ["address"])
def cmd_status(message):
    mybot.send_message(config.TELEGRAM_GROUP_ID, f"Server IP: {s.address}")

#bot checks if we are receiving new messages
def message_loop():
    mybot.infinity_polling()

#login aternos account and search the server
def login_aternos():
    aternos = Client.from_credentials(config.ATERNOS_USER, config.ATERNOS_PASSWORD)
    srvs = aternos.list_servers()
    global s
    s = srvs[0]

#################### MAIN #################### 

if __name__ == '__main__':

    login_aternos()
    
    #we define a thread to execute the function "message_loop()" in the background
    mybot_thread = threading.Thread(name="mybot_thread", target=message_loop) 
    mybot_thread.start()
    print("Bot started")

