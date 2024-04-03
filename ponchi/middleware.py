from typing import Tuple, Any
import importlib

from aiogram.types import Message

from ponchi.config import config
from ponchi.session_controller import SessionController


class Middlewares:
    """
    A class for working with middleware. Implemented singletone
    """
    instance = None

    def __init__(self):
        self.middlewares = []

    async def real_init(self) -> 'Middlewares':
        """
        If this is the first initialization, it initializes all middlewares, if not, it returns an existing object
        """
        if not Middlewares.instance:
            for module in config.MIDDLEWARE:
                self.middlewares.append(
                    await getattr(importlib.import_module(module), module.split('.')[-1].title())().real_init()
                )
            Middlewares.instance = self
            return self
        else:
            return Middlewares.instance

    async def pre_action(self, message: Message, session: SessionController) -> Tuple[Message, SessionController]:
        """
        Sequentially passes a message object
        and a session object to middlewares
        for processing before processing the message
        """
        new_message, new_session = message, session
        for module in self.middlewares:
            new_message, new_session = await module.pre_action(new_message, new_session)

        return new_message, new_session

    async def post_action(self, message: Message, session: SessionController) -> Tuple[Message, SessionController]:
        """
        Sequentially passes a message object
        and a session object to middlewares
        for processing after processing the message
        """
        new_message, new_session = message, session
        for module in self.middlewares:
            new_message, new_session = await module.post_action(new_message, new_session)
        return new_message, new_session


