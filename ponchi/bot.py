import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from .config import config
import ponchi.bot_handler as bot_handler

logger = logging.getLogger('ponchi.bot')

if config.TOKEN == "":
    logger.error("Add token to config")
    exit()

TOKEN = config.TOKEN
dp = Dispatcher()


@dp.message()
async def message(message: types.Message) -> None:
    """
    Redirect all input to bot_handler
    """
    await bot_handler.bot_handler(message)


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

asyncio.run(main())
