import unittest

from file_reader.file_reader import read_file_to_grid
from grid_interpreter.grid_interpreter import find_symbols, find_full_numbers
from logic.logic import check_adjacency_for_numbers_with_coordinates, add_qualified_numbers


class IntegrationTest(unittest.TestCase):
    def test_full_integration(self):
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


if __name__ == '__main__':
    unittest.main()
