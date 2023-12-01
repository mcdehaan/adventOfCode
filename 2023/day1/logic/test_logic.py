import unittest
from logic import read_file_lines, extract_numbers, add_all_numbers, replace_words_with_numbers


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

    def test_replace_words_with_numbers(self):
        test_lines = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen'
        ]
        expected_results = [
            '219',
            '8wo3',
            'abc123xyz',
            'x2ne34',
            '49eight72',
            'z1ight234',
            '7pqrst6teen'
        ]
        results = replace_words_with_numbers(test_lines)
        print(f"\nTest result: {results}")
        self.assertEqual(results, expected_results)

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
        expected_total = 182
        print(f"\nExpected result = {expected_total}")

        result = add_all_numbers(test_cases)
        print(f"Test result: {result}")
        self.assertEqual(result, expected_total)


if __name__ == '__main__':
    unittest.main()
