import unittest

from general_logic import (
    read_file_lines,
    convert_string_to_number,
    find_first_digit,
    find_last_digit,
    extract_numbers,
    add_all_numbers,
)


class TestLogicFunctions(unittest.TestCase):

    def test_read_read_file_lines(self):
        content = read_file_lines('test_input.txt')
        self.assertEqual(content, [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen'
        ])

    def test_read_read_file_error(self):
        content = read_file_lines('doesNotExist.txt')
        self.assertEqual(content, [])

    def test_convert_string_to_number(self):
        results = convert_string_to_number("2")
        expected_result = 2
        print(f"\nExpected result: {expected_result}")
        print(f"Test result: {results}")
        self.assertEqual(results, expected_result)

    def test_find_first_digit(self):
        result = find_first_digit("two91four")
        expected_result = 2
        print(f"\nExpected result: {expected_result}")
        print(f"\nTest result: {result}")
        self.assertEqual(expected_result, result)

    def test_find_last_digit(self):
        result = find_last_digit("two91four")
        expected_result = 4
        print(f"\nExpected result: {expected_result}")
        print(f"\nTest result: {result}")
        self.assertEqual(expected_result, result)

    def test_extract_numbers(self):
        test_cases = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen'
        ]
        expected_results = [
            29, 83, 13, 24, 42, 14, 76
        ]

        results = extract_numbers(test_cases)
        print(f"\nTest result: {results}")
        self.assertEqual(results, expected_results)

    def test_add_all_numbers(self):
        test_cases = [
            29, 83, 13, 24, 42, 14, 76
        ]
        expected_total = 281
        print(f"\nExpected result = {expected_total}")

        result = add_all_numbers(test_cases)
        print(f"Test result: {result}")
        self.assertEqual(result, expected_total)


if __name__ == '__main__':
    unittest.main()
