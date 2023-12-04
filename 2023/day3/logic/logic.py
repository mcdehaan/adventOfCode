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


