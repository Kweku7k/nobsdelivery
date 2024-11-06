import os
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
bot_token = os.getenv('PRESTO_TELEGRAM_BOT_TOKEN')
bot = Bot(token=bot_token)

async def send_message(chat_id = "-4517477711", text="Testing"):
    print(chat_id, text)
    print("Attempting to send order to telegram")
    try:
        # Send a message to the specified chat ID
        await bot.send_message(chat_id=chat_id, text=text)
        print("Order sent successfully")
    except Exception as e:
        print(f"Error sending order: {e}")

# Replace 'YOUR_CHAT_ID' with the chat ID you want to send messages to
chat_id = 'YOUR_CHAT_ID'  # e.g., your user ID or group ID
message = "Hello from my bot!"

# send_message(chat_id, message)