import logging
import os
import telegram

from functools import partial
from dotenv import load_dotenv
from telegram import Update


from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackContext
from telegram.ext import CallbackQueryHandler

logger = logging.getLogger(__name__)


def send_message_to_bot(message):
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('chat_id')
    bot = telegram.Bot(token=token)
    bot.send_message(text=message, chat_id=chat_id)


def start(update: Update, context: CallbackContext, chat_id, user_reply):
    query = update.callback_query
    update.message.reply_text(text='Hi, I flowers shop bot!')


def send_message_update(update, context, chat_id, message):
    bot = context.bot
    bot.send_message(text=f'{chat_id}: {message}', chat_id=chat_id)


def handle_chat(update: Update, context: CallbackContext):
    bot = context.bot
    query = update.callback_query
    chat_id = query.message.chat_id
    message = update.message.text
    bot.send_message(text=message, chat_id=chat_id)


def handle_users_reply(update: Update, context: CallbackContext):

    if update.message:
        user_reply = update.message.text
        chat_id = update.message.chat_id
    elif update.callback_query:
        user_reply = update.callback_query.data
        chat_id = update.callback_query.message.chat_id
    else:
        return

    if user_reply == '/start':
        start(update, context, chat_id, user_reply)
    else:
        send_message(update, context, chat_id, user_reply)


def help(update, callbackcontext):
    update.message.reply_text("Use /start to test this bot.")


def error(update, callbackcontext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start_bot():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    updater = Updater(token)
    dispatcher = updater.dispatcher
    parameters = partial(
                handle_users_reply,
            )
    dispatcher.add_handler(CallbackQueryHandler(parameters))
    dispatcher.add_handler(MessageHandler(Filters.text, parameters))
    dispatcher.add_handler(CommandHandler('start', parameters))
    logger.info('Telegram flowers shop started.')
    updater.start_polling()
    updater.idle()


# def main():
#     send_message('hi bot friend')
#     start_bot()
#
#
# if __name__ == '__main__':
#     main()
