import asyncio
from typing import Any

from .database import DB


class SessionController:

    async def real_init(self) -> 'SessionController':
        """
        Real init.

        It exists because it is impossible to do asynchronous __init__
        """
        self.session = await self.DB.get_session(self.chat_id)
        if '_function' not in self.session.keys():
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
        return self.session[item]

    async def set_data(self, item: str, data: Any) -> None:
        self.session[item] = data

    async def write_session(self) -> None:
        await self.DB.write_session(self.chat_id, self.session)
