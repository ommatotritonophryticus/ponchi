"""
Contains an abstract class for interacting with the database
"""
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
    async def read_data(self, key: str) -> Any:
        """
        Method of get value from database
        """

    @abstractmethod
    async def write_data(self, key: str, value: Any) -> bool:
        """
        Method of set value to database
        """

    @abstractmethod
    async def get_session(self, chat_id: int) -> Dict[str, Any]:
        """
        Method of obtaining session data
        """

    @abstractmethod
    async def write_session(self, chat_id: int, data: Dict[str, Any]) -> bool:
        """
        Method of recording session data
        """
