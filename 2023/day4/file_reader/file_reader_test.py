import unittest
from file_reader import read_and_process_file


class TestFileReaderFunctions(unittest.TestCase):

    def test_read_and_process_file(self):
        expected_result = [
            {'card': 1, 'winning_numbers': [41, 48, 83, 86, 17], 'actual_numbers': [83, 86, 6, 31, 17, 9, 48, 53]},
            {'card': 2, 'winning_numbers': [13, 32, 20, 16, 61], 'actual_numbers': [61, 30, 68, 82, 17, 32, 24, 19]},
            {'card': 3, 'winning_numbers': [1, 21, 53, 59, 44], 'actual_numbers': [69, 82, 63, 72, 16, 21, 14, 1]},
            {'card': 4, 'winning_numbers': [41, 92, 73, 84, 69], 'actual_numbers': [59, 84, 76, 51, 58, 5, 54, 83]},
            {'card': 5, 'winning_numbers': [87, 83, 26, 28, 32], 'actual_numbers': [88, 30, 70, 12, 93, 22, 82, 36]},
            {'card': 6, 'winning_numbers': [31, 18, 13, 56, 72], 'actual_numbers': [74, 77, 10, 23, 35, 67, 36, 11]}
        ]
        result = read_and_process_file('./test_input.txt')
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
