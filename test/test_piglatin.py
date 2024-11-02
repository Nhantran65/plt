import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_initial_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(phrase, translator.retrieve_phrase())

