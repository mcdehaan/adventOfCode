import unittest

from logic import find_lowest_number


class TestLogicFunctions(unittest.TestCase):
    def test_find_lowest_number(self):
        expected_result = 1
        result = find_lowest_number([1, 2, 3])
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
