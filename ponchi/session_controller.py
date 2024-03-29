import asyncio
from typing import Any

from .database import DB


class SessionController:

    async def real_init(self) -> 'SessionController':
        self.session = await DB.get_session(self.chat_id)
        if '_function' not in self.session.keys():
            self.session['_function'] = 'start'
        return self

    def __init__(self, chat_id):
        '''
        Session object
        if session not exist create new session

        :param chat_id:
        '''
        self.session = None
        self.chat_id: int = chat_id

    async def get_data(self, item: str) -> Any:
        return self.session[item]

    async def set_data(self, item: str, data: Any) -> None:
        self.session[item] = data

    async def write_session(self) -> None:
        await DB.write_session(self.chat_id, self.session)
