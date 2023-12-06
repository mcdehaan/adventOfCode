
def read_seeds_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()  # Read the first line and strip any leading/trailing whitespace

        # Splitting the line into key ('seeds') and values (numbers)
        key, numbers_str = first_line.split(': ')

        # Convert the string of numbers into a list of integers
        numbers = [int(num) for num in numbers_str.split()]

        # Return as a dictionary
        return {key: numbers}


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
