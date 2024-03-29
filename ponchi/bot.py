import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from .config import config
import ponchi.bot_handler as bot_handler


if config.TOKEN == "":
    print("Add token to config")
    exit()

TOKEN = config.TOKEN
dp = Dispatcher()


@dp.message()
async def message(message: types.Message) -> None:
    await bot_handler.bot_handler(message)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

asyncio.run(main())
