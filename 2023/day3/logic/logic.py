def check_symbol_adjacency(input_coordinates, input_symbol_coordinates):
    """
        Checks if any digit of the number is adjacent to any of the symbol coordinates in the list.

        :param input_coordinates: Coordinates of each digit of the number (list of tuples).
        :param input_symbol_coordinates: List of coordinates to check against (list of tuples).
        :return: True if adjacent, False otherwise.
        """
    for number_with_coordinates in input_coordinates:
        for coordinate in input_symbol_coordinates:
            if (abs(number_with_coordinates[0] - coordinate[0]) <= 1
                    and abs(number_with_coordinates[1] - coordinate[1]) <= 1):
                return True
    return False


def check_adjacency_for_number_with_coordinates(input_number_with_coordinates, input_symbol_coordinates):
    """
    Checks if any digit of the number is adjacent to any of the coordinates in the list.

    :param input_number_with_coordinates: NumberWithCoordinates object.
    :param input_symbol_coordinates: List of coordinates to check against (list of tuples).
    :return: True if adjacent, False otherwise.
    """
    # Extracting the coordinates from the NumberWithCoordinates object
    number_coordinates = input_number_with_coordinates['coordinates']

    # Using the extracted coordinates to call check_symbol_adjacency
    return check_symbol_adjacency(number_coordinates, input_symbol_coordinates)


def check_adjacency_for_numbers_with_coordinates(input_numbers_with_coordinates, input_symbol_coordinates):
    """
    Checks if any digit of the number is adjacent to any of the coordinates in the list.

    :param input_numbers_with_coordinates: NumberWithCoordinates object.
    :param input_symbol_coordinates: List of coordinates to check against (list of tuples).
    :return: True if adjacent, False otherwise.
    """
    return_numbers_with_coordinates = []

    for number_with_coordinates in input_numbers_with_coordinates:
        if check_adjacency_for_number_with_coordinates(number_with_coordinates, input_symbol_coordinates):
            return_numbers_with_coordinates.append(number_with_coordinates)

    return return_numbers_with_coordinates


def add_qualified_numbers(input_numbers_with_coordinates):
    """
    Adds up the numbers represented as strings in a list of dictionaries.

    :param input_numbers_with_coordinates: List of dictionaries with 'number' as a string and 'coordinates'.
    :return: Total sum of the numbers as an integer.
    """
    total_sum = 0
    for number_with_coordinates in input_numbers_with_coordinates:
        number = int(number_with_coordinates['number'])
        total_sum += number
    return total_sum


def check_gear_adjacency(input_coordinates, input_gear_coordinates):
    """
        Checks if any digit of the number is adjacent to any of the gear coordinates in the list.

        :param input_coordinates: Coordinates of each digit of the number (list of tuples).
        :param input_gear_coordinates: List of coordinates to check against (list of tuples).
        :return: True if adjacent, False otherwise.
        """
    for number_with_coordinates in input_coordinates:
        for coordinate in input_gear_coordinates:
            if (abs(number_with_coordinates[0] - coordinate[0]) <= 1
                    and abs(number_with_coordinates[1] - coordinate[1]) <= 1):
                return True
    return False


def check_two_numbers_one_gear(input_numbers_with_coordinates, input_gear_coordinates):
    """
    Checks if 'check_gear_adjacency' is True for exactly two sets of input_coordinates
    and one set of input_gear_coordinates.

    :param input_numbers_with_coordinates: List of numbers with coordinates (each list is a set of coordinates).
    :param input_gear_coordinates: List of gear coordinates to check against.
    :return: True if exactly two sets of coordinates are adjacent to the gear coordinates, False otherwise.
    """
    true_count = 0

    input_coordinates_sets = []
    for number_with_coordinates in input_numbers_with_coordinates:
        input_coordinates_sets.append(number_with_coordinates['coordinates'])

    for coordinates_set in input_coordinates_sets:
        if check_gear_adjacency(coordinates_set, [input_gear_coordinates]):
            true_count += 1
            if true_count > 2:
                return False  # More than two sets are adjacent, return False immediately

    return true_count == 2


def check_all_working_gears(input_coordinates_sets, input_gears_coordinates):
    """
    Checks if 'check_gear_adjacency' is True for exactly two sets of input_coordinates
    and one set of input_gear_coordinates.

    :param input_coordinates_sets: List of lists of coordinates (each list is a set of coordinates).
    :param input_gears_coordinates: List of lists of gear coordinates to check against.
    :return: True if exactly two sets of coordinates are adjacent to the gear coordinates, False otherwise.
    """
    working_gears = []

    for gear_coordinates in input_gears_coordinates:
        if check_two_numbers_one_gear(input_coordinates_sets, gear_coordinates):
            working_gears.append(gear_coordinates)

    return working_gears


def find_adjacent_numbers_for_gears(numbers_with_coords, gear_coords):
    """
    Finds the two numbers adjacent to each 'working gear'.

    :param numbers_with_coords: List of dictionaries with 'number' and 'coordinates'.
    :param gear_coords: List of coordinates of 'working gears'.
    :return: Dictionary mapping each gear to its two adjacent numbers.
    """
    gear_to_numbers = {}

    for gear in gear_coords:
        adjacent_numbers = []
        for number_entry in numbers_with_coords:
            if check_gear_adjacency(number_entry['coordinates'], [gear]):
                adjacent_numbers.append(number_entry['number'])
                if len(adjacent_numbers) == 2:
                    break
        if len(adjacent_numbers) == 2:
            gear_to_numbers[gear] = adjacent_numbers

    return gear_to_numbers


def multiply_adjacent_numbers(gear_to_numbers):
    """
    Multiplies the number values as integers for each gear and returns them.

    :param gear_to_numbers: Dictionary mapping each gear to its two adjacent numbers.
    :return: Dictionary mapping each gear to the product of its adjacent numbers.
    """
    gear_to_product = {}

    for gear, numbers in gear_to_numbers.items():
        if len(numbers) == 2:
            product = int(numbers[0]) * int(numbers[1])
            gear_to_product[gear] = product

    return gear_to_product


def add_adjacent_multiplied_numbers(gear_to_product):
    """
    Sums up all the multiplied results from the dictionary.

    :param gear_to_product: Dictionary mapping each gear to the product of its adjacent numbers.
    :return: The sum of all the products.
    """
    total_sum = sum(gear_to_product.values())
    return total_sum

