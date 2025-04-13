import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    def setUp(self):
        file = open('../users.json', 'w')
        file.write('[]')
        file.close()

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
    def test_choose_player(self, mock_input, mock_print):
        self.assertEqual(main.choose_player(), "invite")

    @patch('builtins.print')
    @patch('builtins.input', return_value="3")
    def test_main(self, mock_input, mock_print):
        result = main.main()
        mock_print.assert_called_with('Bye')
        self.assertEqual(result, 1)

    def test_games_menu(self):
        pass


if __name__ == '__main__':
    unittest.main()
