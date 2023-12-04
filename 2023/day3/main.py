from file_reader.file_reader import read_file_to_grid
from grid_interpreter.grid_interpreter import find_symbols, find_full_numbers
from logic.logic import check_adjacency_for_numbers_with_coordinates, add_qualified_numbers

# Part 1
if __name__ == '__main__':
    grid = read_file_to_grid('./input.txt')
    symbol_list = find_symbols(grid)
    full_number_list = find_full_numbers(grid)
    adjacent_numbers = check_adjacency_for_numbers_with_coordinates(full_number_list, symbol_list)
    final_result = add_qualified_numbers(adjacent_numbers)
    print(f"\nFinal result: {final_result}")


