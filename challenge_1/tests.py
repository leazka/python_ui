from pick_out_vowels import pick_out_vowels
import unittest


class TestChallenge(unittest.TestCase):
    def test_happy_path(self):
        expected_result = ['e', 'o', 'o', 'a', 'i', 'o', 'a']
        actual_result = pick_out_vowels(sentence="Hello, today is Monday")
        self.assertEqual(actual_result, expected_result)

    def test_pass_integer(self):
        with self.assertRaises(TypeError):
            pick_out_vowels(sentence=1)

    def test_empty_string(self):
        expected_result = []
        actual_result = pick_out_vowels(sentence="")
        self.assertEqual(actual_result, expected_result)

    def test_no_vowels(self):
        expected_result = []
        actual_result = pick_out_vowels(sentence="Thtn gbvp")
        self.assertEqual(actual_result, expected_result)

    def test_case_sensitivity(self):
        expected_result = ['o', 'O', 'E', 'u']
        actual_result = pick_out_vowels(sentence="oO Eu")
        self.assertEqual(actual_result, expected_result)

    def test_special_characters(self):
        expected_result = ['o', 'o', 'o', 'i']
        actual_result = pick_out_vowels(sentence="%good morning!")
        self.assertEqual(actual_result, expected_result)
