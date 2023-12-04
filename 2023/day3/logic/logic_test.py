import unittest

from logic import (check_symbol_adjacency,
                   check_adjacency_for_number_with_coordinates,
                   check_adjacency_for_numbers_with_coordinates,
                   add_qualified_numbers)


class TestLogicFunctions(unittest.TestCase):
    def test_check_adjacent_symbols_success(self):
        number_coordinates = [(2, 6), (2, 7), (2, 8)]
        symbol_coordinates = [(0, 0), (0, 1), (3, 9)]

        expected_result = True
        result = check_symbol_adjacency(number_coordinates, symbol_coordinates)

        self.assertEqual(expected_result, result)

    def test_check_adjacent_symbols_failed(self):
        number_coordinates = [(2, 6), (2, 7), (2, 8)]
        symbol_coordinates = [(0, 0), (0, 1), (4, 9)]

        expected_result = False
        result = check_symbol_adjacency(number_coordinates, symbol_coordinates)

        self.assertEqual(expected_result, result)

    def test_adjacency_for_number_with_coordinates_failed(self):
        number_with_coordinates = {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        symbol_coordinates = [(0, 0), (0, 1), (4, 9)]

        expected_result = False
        result = check_adjacency_for_number_with_coordinates(number_with_coordinates, symbol_coordinates)

        self.assertEqual(expected_result, result)

    def test_adjacency_for_number_with_coordinates_success(self):
        number_with_coordinates = {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        symbol_coordinates = [(0, 0), (0, 1), (8, 8)]

        expected_result = True
        result = check_adjacency_for_number_with_coordinates(number_with_coordinates, symbol_coordinates)

        self.assertEqual(expected_result, result)

    def test_adjacency_for_numbers_with_coordinates(self):
        numbers_with_coordinates = [
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
        symbol_coordinates = [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]

        expected_result = [
            {'number': '467', 'coordinates': [(0, 0), (0, 1), (0, 2)]},
            {'number': '35', 'coordinates': [(2, 2), (2, 3)]},
            {'number': '633', 'coordinates': [(2, 6), (2, 7), (2, 8)]},
            {'number': '617', 'coordinates': [(4, 0), (4, 1), (4, 2)]},
            {'number': '592', 'coordinates': [(6, 2), (6, 3), (6, 4)]},
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '664', 'coordinates': [(9, 1), (9, 2), (9, 3)]},
            {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        ]

        result = check_adjacency_for_numbers_with_coordinates(numbers_with_coordinates, symbol_coordinates)

        self.assertEqual(expected_result, result)

    def test_add_qualified_numbers(self):
        expected_result = 2017
        numbers_with_coordinates = [
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '664', 'coordinates': [(9, 1), (9, 2), (9, 3)]},
            {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        ]

        result = add_qualified_numbers(numbers_with_coordinates)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
