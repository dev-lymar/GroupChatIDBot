import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("API_TOKEN is required but not set in environment variables")

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(message: Message):
    """Echo the chat ID back to the user."""
    try:
        chat_id = message.chat.id
        logger.info(f"Received message from Chat ID: {chat_id}")
        await message.reply(f"Chat ID: {chat_id}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


async def main():
    """Start polling."""
    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
