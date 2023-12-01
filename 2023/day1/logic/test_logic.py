import unittest
from logic import read_input_file, calculate_floor


class TestLogicFunctions(unittest.TestCase):

    def test_read_input_file(self):
        content = read_input_file('test_input.txt')
        self.assertEqual(content, '(()(()(')

    def test_count_brackets(self):
        # Test the count_brackets function
        test_cases = [
            ("()()", 0),
            ("(())", 0),
            ("(((", 3),
            ("(()(()(", 3),
            ("))(((((", 3),
            ("())", -1),
            ("))(", -1),
            (")))", -3),
            (")())())", -3),
        ]

        for input_string, expected_output in test_cases:
            result = calculate_floor(input_string)
            print(f"Test result: {result}")
            self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
