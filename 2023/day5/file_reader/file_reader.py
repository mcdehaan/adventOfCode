import os


def read_seeds_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()  # Read the first line and strip any leading/trailing whitespace

        # Splitting the line into key ('seeds') and values (numbers)
        key, numbers_str = first_line.split(': ')

        # Convert the string of numbers into a list of integers
        numbers = [int(num) for num in numbers_str.split()]

        # Return as a dictionary
        return {key: numbers}


def read_seed_ranges_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()  # Read the first line and strip any leading/trailing whitespace

        parts = first_line.split(': ')
        name = parts[0]
        numbers = [int(num) for num in parts[1].split()]

        # Pairing the numbers and adding them to a list
        data = []
        for i in range(0, len(numbers), 2):
            data.append({'seed_number': numbers[i], 'range': numbers[i + 1]})

        return {'name': name, 'data': data}


def read_maps_from_file(file_path):
    maps = []
    current_map = {}
    map_started = False

    with open(file_path, 'r') as file:
        for line in file:

            # Skip the first line of the file
            if not line.startswith('seeds'):

                line = line.strip()
                if not line:
                    # Empty line indicates the start of a new map or between maps
                    map_started = False
                    continue

                if not map_started:
                    # Start of a new map
                    map_started = True
                    if current_map:
                        # If there's a previous map, add it to the maps list
                        maps.append(current_map)
                    current_map = {'map': line.replace(':', ''), 'data': []}
                else:
                    # Process map data lines
                    dest_start, source_start, length = [int(num) for num in line.split()]
                    current_map['data'].append({
                        'destination range start': dest_start,
                        'source range start': source_start,
                        'range length': length
                    })

        # Add the last map to the list
        if current_map:
            maps.append(current_map)

    return maps


def count_files_in_folder(folder_path):
    """
    Counts the number of files in the specified folder.

    :param folder_path: Path to the folder.
    :return: The number of files in the folder.
    """
    return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])


def add_int_to_file(filename, int_value):
    """
    Adds an integer value to an existing .txt file.

    :param filename: The name of the file to which the integer will be added.
    :param int_value: The integer value to add.
    """
    with open(filename, 'a') as file:
        file.write(f"{int_value}\n")


def read_string_array_from_file(filename):
    """
    Reads a string array from a .txt file.

    :param filename: The name of the file to read.
    :return: A list of strings, each representing a line in the file.
    """
    string_array = []
    with open(filename, 'r') as file:
        for line in file:
            string_array.append(line.strip())

    return string_array


def read_int_from_file(filename):
    """
    Reads an integer value from a file.

    :param filename: The name of the file to read from.
    :return: The integer value read from the file.
    """
    with open(filename, 'r') as file:
        int_value = int(file.read().strip())
    return int_value


def read_first_int_from_file(filename):
    """
    Reads the first integer value from a file.

    :param filename: The name of the file to read from.
    :return: The first integer value read from the file.
    """
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        int_value = int(first_line)
    return int_value


def read_all_ints_and_find_min(filename):
    """
    Reads all integer values from a file and finds the minimum.

    :param filename: The name of the file to read from.
    :return: The minimum integer value in the file.
    """
    with open(filename, 'r') as file:
        int_values = [int(line.strip()) for line in file if line.strip()]
    return min(int_values)

