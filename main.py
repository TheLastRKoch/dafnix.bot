#!/usr/bin/env python


import logging
from os import environ as env
from dotenv import load_dotenv
from command_handlers import current_url, echo, update_url, start, help_command
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Load environment variables
load_dotenv()


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(env["TELEGRAM_BOT_TOKEN"])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Player Feature
    dispatcher.add_handler(CommandHandler("current_url", current_url))
    dispatcher.add_handler(CommandHandler("update_url", update_url))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    updater.start_webhook(
        listen=env["HOST"],
        port=env["PORT"],
        url_path=env["TELEGRAM_BOT_TOKEN"],
        webhook_url='http://yourherokuappname.herokuapp.com/' +
        env["TELEGRAM_BOT_TOKEN"])

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
