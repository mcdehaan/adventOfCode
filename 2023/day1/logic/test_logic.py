import unittest
from logic import read_file_lines, extract_numbers, add_all_numbers


class TestLogicFunctions(unittest.TestCase):

    def test_read_read_file_lines(self):
        content = read_file_lines('test_input.txt')
        self.assertEqual(content, ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'])

    def test_read_read_file_error(self):
        content = read_file_lines('doesNotExist.txt')
        self.assertEqual(content, [])

    def test_extract_digits(self):
        test_cases = [
            "1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"
        ]
        expected_results = [
            12, 38, 15, 77
        ]

        results = extract_numbers(test_cases)
        print(f"\nTest result: {results}")
        self.assertEqual(results, expected_results)

    def test_add_all_numbers(self):
        test_cases = [
            12, 38, 15, 77
        ]
        expected_total = 142
        print(f"\nExpected result = {expected_total}")

        result = add_all_numbers(test_cases)
        print(f"Test result: {result}")
        self.assertEqual(result, expected_total)


if __name__ == '__main__':
    unittest.main()
