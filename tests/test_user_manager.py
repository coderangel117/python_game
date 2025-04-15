import os
import unittest
from unittest.mock import patch

import user_manager


class TestUserManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        user_manager.new_user('invite')

    def test_find_user(self):
        self.assertTrue(user_manager.find_user('invite'))
        self.assertFalse(user_manager.find_user('gab'))

    @patch('builtins.print')
    def test_get_all_users(self, mock_print):
        self.assertEqual(user_manager.get_all_users(), ['invite.json'])

    def test_get_user_files(self):
        users = user_manager.get_user_files()
        self.assertEqual(user_manager.get_user_files(), ['invite.json'])

    def test_merge_json_files(self):
        user_manager.new_user('gab')
        users = user_manager.get_user_files()
        user_manager.merge_json_files(users)
        self.assertTrue(os.path.exists('gab.json'))
        file = open('users.json', 'r')
        self.assertEqual(file.read(), """[
  {
    "username": "invite",
    "played_games": 0,
    "nbfail": 0,
    "nbwin": 0,
    "greatest_score": []
  },
  {
    "username": "gab",
    "played_games": 0,
    "nbfail": 0,
    "nbwin": 0,
    "greatest_score": []
  }
]""")
        file.close()

    @classmethod
    def tearDownClass(cls):
        os.remove('users.json')
        os.remove('gab.json')
        os.remove('invite.json')


if __name__ == '__main__':
    unittest.main()
