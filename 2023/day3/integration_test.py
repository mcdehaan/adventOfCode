import unittest

from file_reader.file_reader import read_file_to_grid
from grid_interpreter.grid_interpreter import find_symbols, find_full_numbers, find_all_gears
from logic.logic import (check_adjacency_for_numbers_with_coordinates,
                         add_qualified_numbers,
                         check_all_working_gears,
                         find_adjacent_numbers_for_gears,
                         multiply_adjacent_numbers,
                         add_adjacent_multiplied_numbers)


class IntegrationTest(unittest.TestCase):
    def test_full_integration_part_1(self):
        expected_result = 4361

        grid = read_file_to_grid('./file_reader/test_input.txt')
        symbol_list = find_symbols(grid)
        print(f"\nSymbol list: {symbol_list}")
        full_number_list = find_full_numbers(grid)
        print(f"\nFull number list: {full_number_list}")
        adjacent_numbers = check_adjacency_for_numbers_with_coordinates(full_number_list, symbol_list)
        print(f"\nAdjacent numbers: {adjacent_numbers}")
        final_result = add_qualified_numbers(adjacent_numbers)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)


    def test_full_integration_part_2(self):
        expected_result = 467835

        grid = read_file_to_grid('./file_reader/test_input.txt')
        gears_list = find_all_gears(grid)
        print(f"\nGear list: {gears_list}")
        full_number_list = find_full_numbers(grid)
        print(f"\nFull number list: {full_number_list}")
        working_gears = check_all_working_gears(full_number_list, gears_list)
        print(f"\nWorking gears: {working_gears}")
        working_gear_numbers = find_adjacent_numbers_for_gears(full_number_list, working_gears)
        print(f"\nWorking gear numbers: {working_gear_numbers}")
        multiplied_adjacent_numbers = multiply_adjacent_numbers(working_gear_numbers)
        print(f"\nMultiplied adjacent numbers: {multiplied_adjacent_numbers}")
        final_result = add_adjacent_multiplied_numbers(multiplied_adjacent_numbers)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)


if __name__ == '__main__':
    unittest.main()
