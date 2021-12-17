from telegram import Update, ForceReply
from telegram.ext import CallbackContext


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
        'You can use the next commands\n/start\n/quick_player')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def quick_player(update: Update, context: CallbackContext) -> None:
    """Update the url of the Quick Player throw an API"""
    update.message.reply_text('Your URL is')
