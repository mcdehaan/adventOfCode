import unittest

from file_reader.file_reader import read_file_to_grid


class IntegrationTest(unittest.TestCase):
    def test_full_integration(self):
        expected_result = 4361
        result = 0

        grid = read_file_to_grid('./input.txt')
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
