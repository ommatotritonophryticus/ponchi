from typing import Callable
from aiogram import types

from ponchi.session_controller import SessionController
from ponchi.application import app


async def bot_handler(message: types.Message) -> None:
    """
    Handles incoming messages from the bot.
    """
    session: SessionController = await SessionController(message.chat.id).real_init()

    current_function: Callable = getattr(app, await session.get_data('_function'))

    next_function: str | Callable = await current_function(
        message,
        session
    )

    if type(next_function) == type(lambda: None):
        next_function: str = next_function.__name__

    await session.set_data('_function', next_function)
    await session.write_session()
