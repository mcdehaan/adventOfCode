import unittest

from file_reader import read_file_to_map


class TestFileReaderFunctions(unittest.TestCase):

    def test_read_seeds_from_file(self):
        expected_result = [
            {'bid': 765, 'hand': [3, 2, 10, 3, 13]},
            {'bid': 684, 'hand': [10, 5, 5, 11, 5]},
            {'bid': 28, 'hand': [13, 13, 6, 7, 7]},
            {'bid': 220, 'hand': [13, 10, 11, 11, 10]},
            {'bid': 483, 'hand': [12, 12, 12, 11, 14]}
        ]
        result = read_file_to_map('./test_input.txt')
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
