import unittest
from file_reader import read_file_to_grid


class TestFileReaderFunctions(unittest.TestCase):

    def test_read_read_file_lines(self):
        expected_result = [
            ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
            ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
            ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
            ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
            ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
        ]
        result = read_file_to_grid('./test_input.txt')
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
