import re
import unittest

from logic.number_word_logic import (
    replace_match,
    replace_first_word_with_number,
    replace_last_word_with_number
)


class TestLogicFunctions(unittest.TestCase):

    def test_replace_match(self):
        test_cases = [
            ("one", "1"),
            ("two", "2"),
            ("ten", "ten"),  # 'ten' is not in the dictionary, should return itself
        ]

        for input_string, expected in test_cases:
            match = re.search(r'\w+', input_string)
            result = replace_match(match)
            self.assertEqual(result, expected, f"Failed on input '{input_string}'")

    def test_replace_first_word_with_number(self):
        test_cases = [
            ('two1nine', '21nine'),
            ('eightwothree', '8wothree'),
            ('abcone2threexyz', 'abc12threexyz'),
            ('xtwone3four', 'x2ne3four'),
            ('4nineeightseven2', '49eightseven2'),
            ('zoneight234', 'z1ight234'),
            ('7pqrstsixteen', '7pqrst6teen'),
        ]
        for input_string, expected_result in test_cases:
            result = replace_first_word_with_number(input_string)
            print(f"\nInput: {input_string}")
            print(f"Expected result: {expected_result}")
            print(f"Test result: {result}")
            self.assertEqual(expected_result, result)

    def test_replace_last_word_with_number(self):
        test_cases = [
            ('two1nine', 'two19'),
            ('eightwothree', 'eightwo3'),
            ('abcone2threexyz', 'abcone23xyz'),
            ('xtwone3four', 'xtwone34'),
            ('4nineeightseven2', '4nineeight72'),
            ('zoneight234', 'zon8234'),
            ('7pqrstsixteen', '7pqrst6teen'),
        ]
        for input_string, expected_result in test_cases:
            result = replace_last_word_with_number(input_string)
            print(f"\nInput: {input_string}")
            print(f"Expected result: {expected_result}")
            print(f"Test result: {result}")
            self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
