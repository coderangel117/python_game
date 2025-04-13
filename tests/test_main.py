import os
import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    def setUp(self):
        file = open('../users.json', 'w')
        file.write('[]')
        file.close()
        self.assertTrue(os.path.exists('../users.json'))
        users = open('../users.json')
        self.assertEqual(users.read(), '[]')
        users.close()

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

    def test_choose_player(self):
        self.assertEqual(main.choose_player(), "invite")

    def test_main(self):
        result = main.main()
        self.assertEqual(result, "bye")

    def test_games_menu(self):
        pass

    def tearDown(self):
        os.remove('../users.json')


if __name__ == '__main__':
    unittest.main()
