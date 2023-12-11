def map_time_distance_from_file(filename):
    """
    Reads a file and maps time and distance data.

    :param filename: The name of the file to read from.
    :return: A list of dictionaries mapping time to distance.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Assuming the first line is for time and the second line is for distance
    times = [int(time) for time in lines[0].split()[1:]]  # Skip the first word 'Time:'
    distances = [int(distance) for distance in lines[1].split()[1:]]  # Skip the first word 'Distance:'

    return [{'time': time, 'distance': distance} for time, distance in zip(times, distances)]
