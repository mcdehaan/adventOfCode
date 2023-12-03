import unittest

from file_reader import (
    read_file
)


class TestLogicFunctions(unittest.TestCase):

    def test_read_read_file_lines(self):
        expected_result = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
        result = read_file('./test_input.txt')
        self.assertEqual(expected_result, result)

    def test_read_read_file_error(self):
        result = read_file('doesNotExist.txt')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
