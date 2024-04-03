"""
Test for databases.redis
"""
import unittest
from unittest.mock import AsyncMock, patch

from ponchi.databases.redis import Database


class TestDB(unittest.IsolatedAsyncioTestCase):
    """
    Unittest class with tests
    """
    def setUp(self):
        self.config = {
            'host': 'localhost',
            'port': 6379,
        }
        self.db = Database(self.config)

    @patch('ponchi.databases.redis.redis.Redis', new_callable=AsyncMock)
    async def test_get_session_existing(self, mock_redis):
        """
        Test the `get_session` method when a session exists in the database.

        Args:
            mock_redis: An AsyncMock representing the Redis connection.

        Returns:
            None
        """
        chat_id = 123
        redis_mock_instance = AsyncMock()
        redis_mock_instance.exists.return_value = True
        redis_mock_instance.hgetall.return_value = {'key1': 'value1', 'key2': 'value2'}
        mock_redis.return_value = redis_mock_instance

        result = await self.db.get_session(chat_id)

        self.assertEqual(result, {'key1': 'value1', 'key2': 'value2'})

    @patch('ponchi.databases.redis.redis.Redis', new_callable=AsyncMock)
    async def test_get_session_non_existing(self, mock_redis):
        """
           Test the `get_session` method when no session exists in the database.

           Args:
               mock_redis: An AsyncMock representing the Redis connection.

           Returns:
               None
           """
        chat_id = 123
        mock_redis_instance = mock_redis.return_value
        mock_redis_instance.exists.return_value = False

        result = await self.db.get_session(chat_id)

        self.assertEqual(result, {})

    @patch('ponchi.databases.redis.redis.Redis', new_callable=AsyncMock)
    async def test_write_session(self, mock_redis):
        """
        Test the `write_session` method.

        Args:
            mock_redis: An AsyncMock representing the Redis connection.

        Returns:
            None
        """
        chat_id = 123
        data = {'key1': 'value1', 'key2': 'value2'}
        mock_redis_instance = mock_redis.return_value

        result = await self.db.write_session(chat_id, data)

        self.assertTrue(result)
        mock_redis_instance.hmset.assert_called_once_with(f'session_{chat_id}', mapping=data)


if __name__ == '__main__':
    unittest.main()
