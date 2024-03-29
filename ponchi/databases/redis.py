from typing import Dict, Any

import redis.asyncio as redis

from .db_interface import DBInterface


class DB(DBInterface):
    def __init__(self, config: Dict[str, Any]):
        self.config: Dict[str, Any] = {key: config[key] for key in config if key != 'type'}

    def _create_connection(self) -> redis.client.Redis:
        return redis.Redis(**self.config)

    async def get_session(self, chat_id: int) -> dict:
        r = await self._create_connection()
        if await r.exists(f'session_{chat_id}'):
            return await r.hgetall(f'session_{chat_id}')
        return {}

    async def write_session(self, chat_id: int, data: Dict[str, Any]) -> bool:
        r = await self._create_connection()
        await r.hmset(f'session_{chat_id}',  mapping=data)
        print(chat_id)
        return True
