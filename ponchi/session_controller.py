import asyncio
from typing import Any
import logging

from .database import DB

logger = logging.getLogger('ponchi.session_controller')


class SessionController:

    async def real_init(self) -> 'SessionController':
        """
        Real init.

        It exists because it is impossible to do asynchronous __init__
        """
        logger.debug('Init session')
        self.session = await self.DB.get_session(self.chat_id)
        if '_function' not in self.session.keys():
            logger.debug('Create new session')
            self.session['_function'] = 'start'
        return self

    def __init__(self, chat_id):
        """
        Sync init
        """
        self.session = None
        self.chat_id: int = chat_id
        self.DB = DB

    async def get_data(self, item: str) -> Any:
        logger.debug('Retrieving session="%d" data by key="%s"', self.chat_id, item)
        return self.session[item]

    async def set_data(self, item: str, data: Any) -> None:
        logger.debug('Writing session="%d" data="%s" by key="%s"', self.chat_id, str(data), item)
        self.session[item] = data

    async def write_session(self) -> None:
        logger.debug('Write session="%d" data in DB', self.chat_id)
        await self.DB.write_session(self.chat_id, self.session)
