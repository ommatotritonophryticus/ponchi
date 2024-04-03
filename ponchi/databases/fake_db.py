"""
Contains a class for FakeDB

DEBUG ONLY
DO NOT USE IN PRODUCTION
"""
from typing import Dict, Any

from .db_interface import DBInterface


class Database(DBInterface):
    """
    Fake DB, to use when there is no possibility to put something good
    """
    def __init__(self, config: Dict[str, Any]):
        self.fake_key_value_database: Dict[str, Any] = {}

    async def read_data(self, key: str) -> Any:
        return self.fake_key_value_database[key]

    async def write_data(self, key: str, value: Any) -> bool:
        self.fake_key_value_database[key] = value
        return True

    async def create_session(self, chat_id) -> Dict[str, Any]:
        """
        Method for create new session
        """
        self.fake_key_value_database[f'session_{chat_id}'] = {}
        return self.fake_key_value_database[f'session_{chat_id}']

    async def get_session(self, chat_id: int) -> Dict[str, Any]:
        if f'session_{chat_id}' in self.fake_key_value_database:
            return self.fake_key_value_database[f'session_{chat_id}']
        return await self.create_session(chat_id)

    async def write_session(self, chat_id: int, data: Dict[str, Any]) -> bool:
        self.fake_key_value_database[f'session_{chat_id}'] = data
        return True
