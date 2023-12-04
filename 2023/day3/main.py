from file_reader.file_reader import read_file_to_grid
from grid_interpreter.grid_interpreter import find_symbols, find_full_numbers, find_all_gears
from logic.logic import check_adjacency_for_numbers_with_coordinates, add_qualified_numbers, check_all_working_gears, \
    find_adjacent_numbers_for_gears, multiply_adjacent_numbers, add_adjacent_multiplied_numbers

# Part 1
if __name__ == '__main__':
    grid = read_file_to_grid('./input.txt')
    symbol_list = find_symbols(grid)
    full_number_list = find_full_numbers(grid)
    adjacent_numbers = check_adjacency_for_numbers_with_coordinates(full_number_list, symbol_list)
    final_result = add_qualified_numbers(adjacent_numbers)
    print(f"\nFinal result: {final_result}")


# Part 2
if __name__ == '__main__':
    grid = read_file_to_grid('./input.txt')
    gears_list = find_all_gears(grid)
    full_number_list = find_full_numbers(grid)
    working_gears = check_all_working_gears(full_number_list, gears_list)
    working_gear_numbers = find_adjacent_numbers_for_gears(full_number_list, working_gears)
    multiplied_adjacent_numbers = multiply_adjacent_numbers(working_gear_numbers)
    final_result = add_adjacent_multiplied_numbers(multiplied_adjacent_numbers)
    print(f"\nFinal result: {final_result}")