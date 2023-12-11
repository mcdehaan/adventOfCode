import unittest

from file_reader import map_time_distance_from_file


class TestFileReaderFunctions(unittest.TestCase):

    def test_read_seeds_from_file(self):
        expected_result = [
             {'distance': 9, 'time': 7},
             {'distance': 40, 'time': 15},
             {'distance': 200, 'time': 30}
        ]
        result = map_time_distance_from_file('./test_input.txt')
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
