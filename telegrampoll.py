import os
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

bot_token = os.getenv('PRESTO_TELEGRAM_BOT_TOKEN')


def start(update, context):
    update.message.reply_text("Hello! I am your bot. How can I help you today?")

def handle_message(update, context):
    text = update.message.text
    update.message.reply_text(f"You said: {text}")

# Initialize bot with token
updater = Updater(token=bot_token, use_context=True)

# Add handlers
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

# Start polling for updates
updater.start_polling()
updater.idle()