# import libraries

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler
import logging
from telegram import InlineQueryResultArticle,InputTextMessageContent
from emoji import emojize

# Updater for updation of given token

update = Updater(token='523770657:AAG5zwwjDthY1wOOXSk9qUMdyXAVjp2oRz8')

# Dispatcher
disp = update.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


                                       # Messages

# Start
def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, feel free to talk to me!")
# Echo
def echo(bot,update):
    if update.message.text!='cake' or update.message.text!='Cake':
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    else:
        cake = emojize(":cake:", use_aliases=True)
        bot.send_message(chat_id=update.message.chat_id,text=cake)
# Love
def love(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="I Love You \n R \n N")
#Hate
def hate(bot,update,args):
    text_agrs = '/'.join(args)
    bot.send_message(chat_id = update.message.chat_id,text = "I Hate Friends like {0}".format(text_agrs))

# Inline Bots
def inline_caps(bot,update):
    query = update.inline_query.query
    if not query:
        return
    res = list()
    res.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'Caps',
            input_message_content = InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id,res)
# Unknown
def unknown(bot,update):
    bot.send_message(chat_id = update.message.chat_id,text = "Sorry , I didn't get that")

                                                      # Handlers
 # Unknown
un_handler = MessageHandler(Filters.command, unknown)
disp.add_handler(un_handler)

  # Inline
inline_handler = InlineQueryHandler(inline_caps)
disp.add_handler(inline_handler)

  #Hate
hate_handler = CommandHandler('hate_t',hate,pass_args=True)
disp.add_handler(hate_handler)

# Love Handler
love_handler = CommandHandler('love_t', love)
disp.add_handler(love_handler)

# Echo Handler
echo_handler = MessageHandler(Filters.text,echo)
disp.add_handler(echo_handler)

# Start Handler
strt_handler = CommandHandler('start', start)
disp.add_handler(strt_handler)

# To start the polling or to update
update.start_polling()