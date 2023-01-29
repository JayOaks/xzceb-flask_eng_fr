# translator.py

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_one(self):
        e2fone = english_to_french('Hello')
        e2ftwo = english_to_french('Bonjour')
        none = english_to_french(None)
        self.assertIsNone(none)
        self.assertEqual(e2fone, "Bonjour")
        self.assertNotEqual(e2ftwo, "Hello")

    def test_two(self):
        f2eone = french_to_english('Bonjour')
        f2etwo = french_to_english('Hello')
        none = french_to_english(None)
        self.assertIsNone(none)
        self.assertEqual(f2eone, "Hello")
        self.assertNotEqual(f2etwo, "Bonjour")


if __name__=='__main__':
	unittest.main()