from typing import Callable
from aiogram import types
import logging

from ponchi.session_controller import SessionController
from ponchi.application import app
from ponchi.middleware import Middlewares

logger = logging.getLogger('ponchi.bot_handler')


async def bot_handler(message: types.Message) -> None:
    """
    Handles incoming messages from the bot.
    """

    logger.debug('Start middlewares init')
    middleware = await Middlewares().real_init()

    logger.debug('Start get session')
    session: SessionController = await SessionController(message.chat.id).real_init()

    logger.debug('Get current session function')
    current_function: Callable = getattr(app, await session.get_data('_function'))

    logger.debug('Make middleware pre-actions ')
    new_message, new_session = await middleware.pre_action(message, session)

    logger.debug('Call function="%s" from application.py', current_function.__name__)
    next_function: str | Callable = await current_function(
        new_message,
        new_session
    )

    logger.debug('Start middleware post-actions')
    new_message, new_session = await middleware.post_action(new_message, new_session)

    if type(next_function) == type(lambda: None):
        next_function: str = next_function.__name__

    logger.debug('Set function="%s" to session=%s', next_function, str(message.chat.id))
    await new_session.set_data('_function', next_function)

    logger.debug('Write data from session=%s', str(message.chat.id))
    await new_session.write_session()
