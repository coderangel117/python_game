import os
import unittest
from unittest.mock import patch

import main
import user_manager


class TestMain(unittest.TestCase):

    def setUp(self):
        user_manager.new_user('gab')
        user_manager.new_user('invite')
        with open('users.json', 'w') as f:
            f.write("""
[
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
            f.close()

    @patch('builtins.print')
    def test_check_win(self, mock_print):
        self.assertTrue(main.check_win([1, 5, "invite", "mystery_number"]))
        mock_print.assert_called_with("You won with 5 attempts")
        self.assertTrue(main.check_win([1, 3, "invite", "shifoumi"]))
        mock_print.assert_called_with("You won with 3 points")
        self.assertFalse(main.check_win([-1, 3, "invite", "mystery_number"]))
        mock_print.assert_called_with("You loose because you doesn't find the number before the last attempt")
        self.assertFalse(main.check_win([-2, 3, "invite", "mystery_number"]))
        mock_print.assert_called_with('You loose because you are a monkey')

    @patch('builtins.print')
    @patch('builtins.input', return_value='')
    def test_choose_player_invite(self, mock_input, mock_print):
        self.assertEqual(main.choose_player(), "invite")
        mock_input.assert_called_with('Which player do you want to play with ? \n')
        mock_print.assert_called_with("Great ! You play as invite \nWARNING: The game won't count in user's stat ")

    @patch('builtins.print')
    @patch('builtins.input', return_value='gab')
    def test_choose_player_ok(self, mock_input, mock_print):
        self.assertEqual(main.choose_player(), "gab")
        mock_input.assert_called_with('Which player do you want to play with ? \n')
        mock_print.assert_called_with("Great ! You play as gab ")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['foo', ''])
    def test_choose_player_ko(self, mock_input, mock_print):
        self.assertEqual(main.choose_player(), "invite")
        mock_input.assert_called_with('Player not found, try again \n')
        mock_print.assert_called_with("Great ! You play as invite \nWARNING: The game won't count in user's stat ")

    @patch('builtins.print')
    @patch('builtins.input', return_value="3")
    def test_main(self, mock_input, mock_print):
        self.assertEqual(main.main(), 1)
        mock_print.assert_called_with('Bye')

    @patch('builtins.print')
    @patch('builtins.input', return_value="4")
    def test_games_menu_return(self, mock_input, mock_print):
        self.assertEqual(main.games_menu(), "main")
        mock_input.assert_called_with('''
            [1] - Mystery number
            [2] - Rock paper scissors
            [3] - Tic Tac Toe
            [4] - return to main menu
            ''')

    def tearDown(self):
        os.remove('users.json')
        os.remove('gab.json')
        os.remove('invite.json')


if __name__ == '__main__':
    unittest.main()
