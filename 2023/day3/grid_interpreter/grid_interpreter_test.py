import unittest

from grid_interpreter import find_symbols, find_numbers, find_full_numbers, extract_full_number, find_all_gears

input_grid = [
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


class TestGridInterpreterFunctions(unittest.TestCase):

    def test_find_symbols(self):
        expected_result = [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]
        result = find_symbols(input_grid)
        self.assertEqual(expected_result, result)

    def test_find_numbers(self):
        expected_result = [(0, 0), (0, 1), (0, 2), (0, 5), (0, 6), (0, 7), (2, 2), (2, 3), (2, 6), (2, 7), (2, 8),
                           (4, 0), (4, 1), (4, 2), (5, 7), (5, 8), (6, 2), (6, 3), (6, 4), (7, 6), (7, 7), (7, 8),
                           (9, 1), (9, 2), (9, 3), (9, 5), (9, 6), (9, 7)]
        result = find_numbers(input_grid)
        self.assertEqual(expected_result, result)

    def test_find_all_gears(self):
        expected_result = [(1, 3), (4, 3), (8, 5)]
        result = find_all_gears(input_grid)
        self.assertEqual(expected_result, result)

    def test_extract_full_number(self):
        expected_result = ('633', [(2, 6), (2, 7), (2, 8)])
        result = extract_full_number(input_grid, 2, 6)
        self.assertEqual(expected_result, result)

    def test_find_full_numbers(self):
        expected_result = [
            {'number': '467', 'coordinates': [(0, 0), (0, 1), (0, 2)]},
            {'number': '114', 'coordinates': [(0, 5), (0, 6), (0, 7)]},
            {'number': '35', 'coordinates': [(2, 2), (2, 3)]},
            {'number': '633', 'coordinates': [(2, 6), (2, 7), (2, 8)]},
            {'number': '617', 'coordinates': [(4, 0), (4, 1), (4, 2)]},
            {'number': '58', 'coordinates': [(5, 7), (5, 8)]},
            {'number': '592', 'coordinates': [(6, 2), (6, 3), (6, 4)]},
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '664', 'coordinates': [(9, 1), (9, 2), (9, 3)]},
            {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        ]
        result = find_full_numbers(input_grid)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
