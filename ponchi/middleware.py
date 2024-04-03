"""
Contains a middleware handler class
"""
from typing import Tuple
import importlib
import logging

from aiogram.types import Message

from ponchi.config import config
from ponchi.session_controller import SessionController

logger = logging.getLogger('ponchi.middleware')


class Middlewares:
    """
    A class for working with middleware. Implemented singletone
    """

    _instance = None

    def __init__(self):
        self.middlewares = []

    async def real_init(self) -> 'Middlewares':
        """
        If this is the first initialization,
        it initializes all middlewares,
        if not, it returns an existing object
        """
        if not Middlewares._instance:
            logger.debug('First init middleware')
            for module in config.MIDDLEWARE:
                self.middlewares.append(
                    await getattr(
                        importlib.import_module(module),
                        module.split('.')[-1].title()
                    )().real_init()
                )
            logger.debug('Finish init')
            Middlewares._instance = self
            return self

        logger.debug('Get exists Middleware instance')
        return Middlewares._instance

    async def pre_action(self,
                         message: Message,
                         session: SessionController
                         ) -> Tuple[Message, SessionController]:
        """
        Sequentially passes a message object
        and a session object to middlewares
        for processing before processing the message
        """
        new_message, new_session = message, session
        for module in self.middlewares:
            logger.debug(
                'Start pre-action middleware="%s"',
                module.__class__.__name__
            )
            new_message, new_session = await module.pre_action(new_message, new_session)

        return new_message, new_session

    async def post_action(self,
                          message: Message,
                          session: SessionController
                          ) -> Tuple[Message, SessionController]:
        """
        Sequentially passes a message object
        and a session object to middlewares
        for processing after processing the message
        """
        new_message, new_session = message, session
        for module in self.middlewares:
            logger.debug(
                'Start post-action middleware="%s"',
                module.__class__.__name__)
            new_message, new_session = await module.post_action(new_message, new_session)
        return new_message, new_session
