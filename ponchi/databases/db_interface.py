from abc import ABC, abstractmethod
from typing import Dict, Any


class DBInterface(ABC):
    """
    Interface for accessing the database
    """
    @abstractmethod
    def __init__(self, config: Dict[str, Any]):
        ...

    @abstractmethod
    async def get_session(self, chat_id: int) -> Dict[str, Any]:
        """
        Method of obtaining session data
        """
        ...

    @abstractmethod
    async def write_session(self, chat_id: int, data: Dict[str, Any]) -> bool:
        """
        Method of recording session data
        """
        ...
