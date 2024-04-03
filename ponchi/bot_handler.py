import importlib
from typing import Callable
from aiogram import types

from ponchi.session_controller import SessionController
from ponchi.application import app
from ponchi.config import config
from ponchi.middleware import Middlewares


async def bot_handler(message: types.Message) -> None:
    """
    Handles incoming messages from the bot.
    """
    middleware = await Middlewares().real_init()

    session: SessionController = await SessionController(message.chat.id).real_init()

    current_function: Callable = getattr(app, await session.get_data('_function'))

    new_message, new_session = await middleware.pre_action(message, session)

    next_function: str | Callable = await current_function(
        new_message,
        new_session
    )

    new_message, new_session = await middleware.post_action(new_message, new_session)

    if type(next_function) == type(lambda: None):
        next_function: str = next_function.__name__

    await new_session.set_data('_function', next_function)
    await new_session.write_session()
