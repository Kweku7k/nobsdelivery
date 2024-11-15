from telegram.ext import Application, CommandHandler, MessageHandler
from telegram import filters

def start(update, context):
    update.message.reply_text("Hello, welcome to PrestoDelivery!")

def main():
    application = Application.builder().token("YOUR_TOKEN_HERE").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == "__main__":
    main()