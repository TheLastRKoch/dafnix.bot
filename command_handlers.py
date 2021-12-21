from telegram import Update, ForceReply
from telegram.ext import CallbackContext

from services import DafnixAPIService, URLService


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'You can use the next commands\n/start\n\n\nPlayer features\n/current_url\n/update_url url')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def current_url(update: Update, context: CallbackContext) -> None:
    api_service = DafnixAPIService()
    message = api_service.get_URL()
    update.message.reply_text(message)


def update_url(update: Update, context: CallbackContext) -> None:
    """Update the url of the Quick Player throw an API"""
    url_service = URLService()
    api_service = DafnixAPIService()

    text = update.message.text
    result = url_service.get_url(text)

    if ("Error:" in result):
        update.message.reply_text(result)

    message = api_service.update_url(result)
    update.message.reply_text(message)
