from abc import ABC, abstractmethod
from typing import Dict, Any


class DBInterface(ABC):
    @abstractmethod
    def __init__(self, config: Dict[str, Any]):
        ...

    @abstractmethod
    async def get_session(self, chat_id: int) -> dict:
        ...

    @abstractmethod
    async def write_session(self, chat_id: int, data: Dict[str, Any]) -> bool:
        ...
