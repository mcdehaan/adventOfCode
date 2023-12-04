

def find_symbols(input_grid):
    symbol_coords = []
    for row_index, row in enumerate(input_grid):
        for col_index, item in enumerate(row):
            if not item.isdigit() and item != '.':
                symbol_coords.append((row_index, col_index))
    return symbol_coords


def find_numbers(input_grid):
    number_coords = []
    for row_index, row in enumerate(input_grid):
        for col_index, item in enumerate(row):
            if item.isdigit():
                number_coords.append((row_index, col_index))
    return number_coords


def extract_full_number(grid, row, col):
    number = ''
    coords_list = []
    while col < len(grid[row]) and grid[row][col].isdigit():
        number += grid[row][col]
        coords_list.append((row, col))
        col += 1  # Move to the next column

    return number, coords_list


def find_full_numbers(grid):
    number_coordinates = []

    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            # Start extraction only if it's a digit and either the first column
            # or the previous column is not a digit
            if item.isdigit() and (column_index == 0 or not row[column_index - 1].isdigit()):
                full_number, coordinates_list = extract_full_number(grid, row_index, column_index)
                number_coordinates.append({'number': full_number, 'coordinates': coordinates_list})

    return number_coordinates





