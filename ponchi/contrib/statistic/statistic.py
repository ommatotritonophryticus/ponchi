"""
Contains the middleware class Statistic
"""
import datetime
import json
from typing import Tuple

from aiogram.types import Message

from ponchi.contrib.base_middleware.base_middleware import BaseMiddleware
from ponchi.session_controller import SessionController


class Statistic(BaseMiddleware):
    """
    Example middleware. Maybe finish it later.
    """
    def __init__(self):
        self.data = {
            'functions': {},
            'log': []
        }

    async def real_init(self, *args, **kwargs) -> 'BaseMiddleware':
        """
        In this case, there are no
        asynchronous operations during
        initialization, so we just return self.
        """
        return self

    async def pre_action(self,
                         message: Message,
                         session: SessionController
                         ) -> Tuple[Message, SessionController]:
        """
        This function simply records
        information about the called functions
        """
        current_session: int = message.chat.id
        current_function: int = await session.get_data('_function')
        try:
            self.data['functions'][current_function] += 1
        except KeyError:
            self.data['functions'][current_function] = 1
        self.data['log'].append({
            'user': current_session,
            'function': current_function,
            'timestamp': str(datetime.datetime.now())
        })
        return message, session

    async def post_action(self,
                          message: Message,
                          session: SessionController
                          ) -> Tuple[Message, SessionController]:
        """
        This function write information in database
        """
        await session.database.write_data('statistic', json.dumps(self.data))
        return message, session
