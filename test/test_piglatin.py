import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_initial_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(phrase, translator.retrieve_phrase())

    def test_empty_string_translation(self):
        phrase = ""
        expected_translation = "nil"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

