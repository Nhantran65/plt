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

    def test_translate_word_with_y(self):
        phrase = "any"
        expected_translation = "anynay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())


    def test_translate_word_with_vowel_end(self):
        phrase = "apple"
        expected_translation = "appleyay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

    def test_translate_word_with_consonant_end(self):
        phrase = "ask"
        expected_translation = "askay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

    def test_translate_starting_with_consonant(self):
        phrase = "hello"
        expected_translation = "ellohay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

    def test_translate_multiple_consonants_start(self):
        phrase = "known"
        expected_translation = "ownknay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

    def test_translate_multiple_words(self):
        phrase = "hello world"
        expected_translation = "ellohay orldway"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

    def test_translate_hyphenated_words(self):
        phrase = "well-being"
        expected_translation = "ellway-eingbay"
        translator = PigLatin(phrase=phrase)
        self.assertEqual(expected_translation, translator.convert())

