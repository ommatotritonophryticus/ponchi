"""
Aiogram bot
All incoming messages
are redirected to bot_handler
"""
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from ponchi import bot_handler
from .config import config

logger = logging.getLogger('ponchi.bot')

if config.TOKEN == "":
    logger.error("Add token to config")
    sys.exit(1)

TOKEN = config.TOKEN
dp = Dispatcher()


@dp.message()
async def message(aiogram_message: types.Message) -> None:
    """
    Redirect all input to bot_handler
    """
    await bot_handler.bot_handler(aiogram_message)


async def main() -> None:
    """
    The function that launches the bot
    """
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

asyncio.run(main())
