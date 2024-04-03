"""
Test for databases.fake_db
"""
import unittest
from ponchi.databases.fake_db import Database


class TestDB(unittest.IsolatedAsyncioTestCase):
    """
    Unittest class with tests
    """
    async def test_create_session(self):
        """
        Tests that create_session creates a new session for a chat_id if it doesn't exist.
        """
        # Use an empty config for testing
        db = Database({})

        chat_id = 123
        session = await db.create_session(chat_id)

        # Verify empty session
        self.assertEqual(session, {})
        # Check session creation
        self.assertIn(f'session_{chat_id}', db.fake_key_value_database)

    async def test_get_session_existing(self):
        """
        Tests that get_session returns the existing session for a chat_id.
        """
        db = Database({})
        chat_id = 456

        # Create a session beforehand
        session_data = {'key': 'value'}
        db.fake_key_value_database[f'session_{chat_id}'] = session_data

        retrieved_session = await db.get_session(chat_id)

        # Verify correct retrieval
        self.assertEqual(retrieved_session, session_data)

    async def test_get_session_nonexistent(self):
        """
        Tests that get_session creates a new session if one doesn't exist for the chat_id.
        """
        db = Database({})
        chat_id = 789

        new_session = await db.get_session(chat_id)

        # Verify empty session creation
        self.assertEqual(new_session, {})
        # Check new session creation
        self.assertIn(f'session_{chat_id}', db.fake_key_value_database)

    async def test_write_session(self):
        """
        Tests that write_session updates the session data for a chat_id.
        """
        db = Database({})
        chat_id = 0

        # Create a session initially
        await db.create_session(chat_id)

        new_data = {'updated': True}
        await db.write_session(chat_id, new_data)

        # Verify data update
        self.assertEqual(db.fake_key_value_database[f'session_{chat_id}'], new_data)


if __name__ == '__main__':
    unittest.main()
