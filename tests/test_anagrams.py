from unittest import TestCase
from anagrams.reverses_text import revers_text, revers_word
from anagrams.reverses_text import CustomTypeError

ATYPICAL_CASES = [
    123,
    {1: 'dfjvndkvjn'},
    ['123']
]


class TestAnagramWord(TestCase):
    def test_typical_behavior(self) -> None:
        cases = [
            ('abcd', 'dcba'),
            ('a1bcd', 'd1cba'),
            ('111', '111'),
            ('$$$', '$$$'),
            ('', ''),
        ]
        for word, expected_result in cases:
            with self.subTest(word=word):
                self.assertEqual(revers_word(word=word), expected_result)

    def test_atypical_behavior(self) -> None:
        for word in ATYPICAL_CASES:
            with self.subTest(word=word):
                self.assertRaises(CustomTypeError, revers_word, word)


class TestAnagramText(TestCase):
    def test_typical_behavior(self) -> None:
        cases = [
            ('', ''),
            ('abcd efgh', 'dcba hgfe'),
            ('a1bcd efg!h', 'd1cba hgf!e'),
            ('111 !!!', '111 !!!'),
        ]
        for text, expected_result in cases:
            with self.subTest(text=text):
                self.assertEqual(revers_text(text=text), expected_result)

    def test_atypical_behavior(self) -> None:
        for text in ATYPICAL_CASES:
            with self.subTest(text=text):
                self.assertRaises(CustomTypeError, revers_text, text)
