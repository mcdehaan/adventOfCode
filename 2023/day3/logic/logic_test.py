import unittest

from logic import (check_symbol_adjacency,
                   check_adjacency_for_number_with_coordinates,
                   check_adjacency_for_numbers_with_coordinates,
                   add_qualified_numbers,
                   check_gear_adjacency,
                   check_two_numbers_one_gear,
                   check_all_working_gears)


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

    def test_gear_adjacency_for_number_with_coordinates_success(self):
        number_with_coordinates = {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        gear_coordinates = [(1, 3), (4, 3), (8, 5)]

        expected_result = True
        result = check_gear_adjacency(number_with_coordinates['coordinates'], gear_coordinates)

        self.assertEqual(expected_result, result)

    def test_gear_adjacency_for_number_with_coordinates_failed(self):
        number_with_coordinates = {'number': '633', 'coordinates': [(2, 6), (2, 7), (2, 8)]}
        gear_coordinates = [(1, 3), (4, 3), (8, 5)]

        expected_result = False
        result = check_gear_adjacency(number_with_coordinates['coordinates'], gear_coordinates)

        self.assertEqual(expected_result, result)

    def test_check_two_numbers_one_gear_success(self):
        numbers_with_coordinates = [
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '664', 'coordinates': [(9, 1), (9, 2), (9, 3)]},
            {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]}
        ]
        input_gear_coordinates = (8, 5)

        input_coordinates_sets = []
        for number_with_coordinates in numbers_with_coordinates:
            input_coordinates_sets.append(number_with_coordinates['coordinates'])

        result = check_two_numbers_one_gear(input_coordinates_sets, input_gear_coordinates)

        self.assertEqual(True, result)

    def test_check_one_numbers_one_gear_failed(self):
        numbers_with_coordinates = [
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '664', 'coordinates': [(9, 1), (9, 2), (9, 3)]},
            {'number': '35', 'coordinates': [(2, 2), (2, 3)]},
        ]
        input_gear_coordinates = (1, 3)

        input_coordinates_sets = []
        for number_with_coordinates in numbers_with_coordinates:
            input_coordinates_sets.append(number_with_coordinates['coordinates'])

        result = check_two_numbers_one_gear(input_coordinates_sets, input_gear_coordinates)

        self.assertEqual(False, result)

    def test_check_three_numbers_one_gear_failed(self):
        numbers_with_coordinates = [
            {'number': '755', 'coordinates': [(7, 6), (7, 7), (7, 8)]},
            {'number': '598', 'coordinates': [(9, 5), (9, 6), (9, 7)]},
            {'number': '35', 'coordinates': [(8, 6), (8, 7)]},
        ]
        input_gear_coordinates = (8, 5)

        input_coordinates_sets = []
        for number_with_coordinates in numbers_with_coordinates:
            input_coordinates_sets.append(number_with_coordinates['coordinates'])

        result = check_two_numbers_one_gear(input_coordinates_sets, input_gear_coordinates)

        self.assertEqual(False, result)

    def test_check_all_working_gears(self):
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
        input_gear_coordinates_sets = [(1, 3), (4, 3), (8, 5)]

        result = check_all_working_gears(numbers_with_coordinates, input_gear_coordinates_sets)
        expected_result = [(1, 3), (8, 5)]

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
