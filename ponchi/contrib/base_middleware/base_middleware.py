from typing import Tuple
from abc import ABC

from aiogram.types import Message

from ponchi.session_controller import SessionController
from ponchi.config import config


class BaseMiddleware(ABC):
    """
    Base class for middleware.
    """

    config = config

    async def real_init(self, *args, **kwargs) -> 'BaseMiddleware':
        """
        Async init.
        """
        return self

    async def pre_action(self, message: Message, session: SessionController) -> Tuple[Message, SessionController]:
        """
        Action before passing the message and session to the function.
        """
        return message, session

    async def post_action(self, message: Message, session: SessionController) -> Tuple[Message, SessionController]:
        """
        Action after passing the message and session to the function.
        """
        return message, session
