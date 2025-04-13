import unittest

import utils


class TestUtils(unittest.TestCase):

    def test_check_special_characters(self):
        self.assertFalse(utils.check_special_characters(""))
        self.assertFalse(utils.check_special_characters("a1"))
        self.assertFalse(utils.check_special_characters("a¹"))
        self.assertFalse(utils.check_special_characters("$/*"))
        self.assertFalse(utils.check_special_characters("1*"))
        self.assertTrue(utils.check_special_characters("1"))

    if __name__ == '__main__':
        unittest.main()
