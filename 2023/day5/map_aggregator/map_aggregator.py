from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import os, time

from file_reader.file_reader import add_int_to_file, read_int_from_file


def get_map_data(input_maps, input_map_title):
    """
    Fetches the data object for a specific map from the list of maps.

    :param input_maps: List of map dictionaries.
    :param input_map_title: Title of the map to fetch data for.
    :return: Data object for the specified map, or None if not found.
    """
    for input_map in input_maps:
        if input_map['map'] == input_map_title:
            return input_map['data']
    return None


def get_map_ranges(input_maps, input_map_title):
    """
    Fetches the data object for a specific map from the list of maps.

    :param input_maps: List of map dictionaries.
    :param input_map_title: Title of the map to fetch data for.
    :return: Ranges object for the specified map, or None if not found.
    """
    for input_map in input_maps:
        if input_map['map'] == input_map_title:
            return input_map['ranges']
    return None


def create_total_converter_list(map_entries):
    """
    Creates a list of source-destination pairs extended by the range.

    :param map_entries: List of map entries with destination range start, range length, and source range start.
    :return: Dictionary containing a list of source-destination pairs.
    """
    ranges = []

    for entry in map_entries:
        destination_start = entry['destination range start']
        source_start = entry['source range start']
        range_length = entry['range length']

        for i in range(range_length):
            source = source_start + i
            destination = destination_start + i
            ranges.append({'source': source, 'destination': destination})

    return {'ranges': ranges}


def update_map_with_converter_list(existing_map, converter_list):
    """
    Updates an existing map with the range mappings from the converter list.

    :param existing_map: The existing map to update.
    :param converter_list: The output from create_total_converter_list, containing range mappings.
    :return: Updated map.
    """
    # Assuming the existing_map has a key 'data' which is a list of mappings
    # and converter_list has a key 'ranges' with the new mappings
    if 'ranges' in converter_list and 'data' in existing_map:
        existing_map['ranges'] = converter_list['ranges']
    return existing_map


def expand_map(existing_map, all_maps):
    map_entries = get_map_data(all_maps, existing_map['map'])
    converter_list = create_total_converter_list(map_entries)
    expanded_map = update_map_with_converter_list(existing_map, converter_list)
    return expanded_map


def expand_all_maps(all_maps):
    with ThreadPoolExecutor() as executor:
        # Submitting all map expansion tasks to the executor
        future_to_map = {executor.submit(expand_map, existing_map, all_maps): existing_map for existing_map in all_maps}

        completed_tasks = 0
        total_tasks = len(all_maps)

        for future in as_completed(future_to_map):
            completed_tasks += 1
            progress = (completed_tasks / total_tasks) * 100
            print(f"Progress: {completed_tasks}/{total_tasks} maps processed ({progress:.2f}%)")

            expanded_map = future.result()
            # replace existing map with expanded map in all_maps
            index = all_maps.index(future_to_map[future])
            all_maps[index] = expanded_map

    return all_maps


def calculate_source_in_range(source, range_start, range_length, destination_start):
    """
    Calculates if the source value is within the given range.

    :param destination_start: The start of the destination range.
    :param source: The source value to check.
    :param range_start: The start of the range.
    :param range_length: The length of the range.
    :return: The destination value if the source is within the range, otherwise the source value as destination value.
    """
    destination = source
    if range_start <= source <= range_start + range_length:
        destination = destination_start + (source - range_start)

    return destination


def source_destination_conversion_for_single_value(existing_map, source_value):
    """
    Converts a single source value based on the existing map.

    :param existing_map: Map dictionary containing 'ranges'.
    :param source_value: The source value to convert.
    :return: The converted destination value.
    """
    destination_values = []
    for range_entry in existing_map.get('data', []):
        destination_values.append(calculate_source_in_range(
            source_value,
            range_entry['source range start'],
            range_entry['range length'],
            range_entry['destination range start']
        ))

    for destination_value in destination_values:
        if destination_value != source_value:
            return destination_value

    return source_value


def process_source_values_async(existing_map, source_values):
    """
    Processes source values asynchronously and returns their corresponding destination values.

    :param existing_map: Map dictionary containing 'ranges'.
    :param source_values: List of source values to convert.
    :return: List of converted destination values.
    """
    destination_values = []
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        future_to_source = {
            executor.submit(source_destination_conversion_for_single_value, existing_map, source_value): source_value
            for source_value in source_values}

        completed_tasks = 0
        total_tasks = len(source_values)
        for future in as_completed(future_to_source):
            completed_tasks += 1
            progress = (completed_tasks / total_tasks) * 100
            # print(f"Progress: {completed_tasks}/{total_tasks} values processed ({progress:.2f}%)")
            destination_values.append(future.result())

    return destination_values


def process_map(map_order_item, expanded_maps, seed_values):
    position = map_order_item['position']
    name = map_order_item['name']
    # print(f"\nProcessing map: {position}: {name}")

    current_map = next((map for map in expanded_maps if map['map'] == name), None)
    if current_map is not None:
        return source_destination_conversion_for_single_value(current_map, seed_values)
    else:
        print(f"Map named {name} not found.")
        return seed_values


def iterate_seeds_trough_maps(existing_maps, seed_values):
    result_values = seed_values

    map_order = [
        {'position': 0, 'name': 'seed-to-soil map'},
        {'position': 1, 'name': 'soil-to-fertilizer map'},
        {'position': 2, 'name': 'fertilizer-to-water map'},
        {'position': 3, 'name': 'water-to-light map'},
        {'position': 4, 'name': 'light-to-temperature map'},
        {'position': 5, 'name': 'temperature-to-humidity map'},
        {'position': 6, 'name': 'humidity-to-location map'}
    ]

    for order in map_order:
        position = order['position']
        name = order['name']
        # print("\n--------------------------------------------")
        # print(f"Processing map: \n{position}: {name}")

        # Find the map by name in the existing_maps list
        current_map = next((map for map in existing_maps if map['map'] == name), None)
        result_values = process_source_values_async(current_map, result_values)
        # print(f"\nResult values: \n{result_values}")

    return result_values


def process_seed(seed_number, seed_range):
    # Same implementation as before
    return [seed_number + i for i in range(seed_range)]


def save_to_file(filename, data):
    """
    Saves data to a file. Data can be a single integer or a list of integers.

    :param filename: Name of the file.
    :param data: Data to be saved (single integer or list of integers).
    """
    with open(filename, 'w') as file:
        if isinstance(data, int):
            file.write(str(data) + '\n')
        else:
            file.write(' '.join(map(str, data)) + '\n')


def process_seed_batch(seed_number, start, end):
    """
    Processes a batch of seeds and returns the range.

    :param seed_number: The starting seed number.
    :param start: The start index of the batch.
    :param end: The end index of the batch.
    :return: List of numbers for the given seed batch.
    """
    return [seed_number + i for i in range(start, end)]


def list_all_seeds(seed_data):
    filenames = []
    with ThreadPoolExecutor() as executor:
        futures = []
        total_batches = sum((seed_info['range'] - 1) // 10000 + 1 for seed_info in seed_data['data'])
        prep_batch_counter = 0
        process_batch_counter = 0

        for seed_info in seed_data['data']:
            seed_number = seed_info['seed_number']
            seed_range = seed_info['range']

            # Splitting the range into batches
            for start in range(0, seed_range, 10000):
                end = min(start + 10000, seed_range)
                prep_batch_counter += 1
                progress = (prep_batch_counter / total_batches) * 100
                print(f"Preparing batches: {progress:.2f}%")
                batch_future = executor.submit(process_seed_batch, seed_number, start, end)
                futures.append(batch_future)

        for future in as_completed(futures):
            process_batch_counter += 1
            progress = (process_batch_counter / total_batches) * 100
            print(f"Batch processing progress: {progress:.2f}%")

            # Saving the result to a file
            seed_result = future.result()
            filename = f"seed_files/seed_{seed_result[0]}_batch_{seed_result[0] + len(seed_result) - 1}.txt"
            save_to_file(filename, seed_result)
            filenames.append(filename)


def process_seeds_file(filename, existing_maps):
    """
    Processes a single seed file.

    :param filename: The file containing seed numbers.
    :param existing_maps: The maps to be used for processing.
    :return: The lowest result from the processed seeds.
    """
    with open(filename, 'r') as file:
        seeds = [int(seed) for seed in file.read().split()]

    lowest_result = float('inf')
    for seed in seeds:
        result = iterate_seeds_trough_maps(existing_maps, [seed])
        lowest_result = min(lowest_result, min(result))

    return lowest_result


def run_process_seeds_files_parallel(start_index, number_of_files_to_process, file_list, existing_maps):
    """
    Executes process_seeds_file on multiple threads in parallel.

    :param start_index: The index of the first file to process.
    :param number_of_files_to_process: Total number of files to process.
    :param file_list: List of files to process.
    :param existing_maps: The maps to be used for processing.
    :param max_threads: Maximum number of threads to use.
    """
    # Calculate the end index and limit the file list
    end_index = min(start_index + number_of_files_to_process, len(file_list))
    limited_file_list = file_list[start_index:end_index]

    with ProcessPoolExecutor() as executor:
        # Submit tasks for the limited file list
        future_to_file = {executor.submit(process_seeds_file, f"seed_files/{file}", existing_maps): file for file in
                          limited_file_list}

        results = []
        completed_tasks = 0
        for future in as_completed(future_to_file):
            # Wait for the future to complete and get the result
            result = future.result()
            results.append(result)
            completed_tasks += 1
            progress = (completed_tasks / len(limited_file_list)) * 100
            print(f"Progress: {completed_tasks}/{len(limited_file_list)} files processed ({progress:.2f}%)")

    print(f"Results: {results}, Start index: {start_index}, End index: {end_index}")
    return min(results)


def process_all_seed_files(seed_files_directory, existing_maps):
    lowest_results = []
    futures_to_files = {}

    with ProcessPoolExecutor() as executor:
        # Initialize a counter for the number of files submitted for processing
        submitted_files = 0
        total_files = len([f for f in os.listdir(seed_files_directory) if f.endswith(".txt")])

        # Submitting file processing tasks to the executor
        for filename in os.listdir(seed_files_directory):
            if filename.endswith(".txt"):
                full_path = os.path.join(seed_files_directory, filename)
                future = executor.submit(process_seeds_file, full_path, existing_maps)
                futures_to_files[future] = filename
                submitted_files += 1
                print(f"Submitted {submitted_files}/{total_files} files for processing")

        completed_tasks = 0
        for future in as_completed(futures_to_files):
            completed_tasks += 1
            progress = (completed_tasks / total_files) * 100
            print(f"Progress: {completed_tasks}/{total_files} files processed ({progress:.2f}%)")

            # Getting the result and the corresponding filename
            lowest_result = future.result()
            lowest_results.append(lowest_result)

    return lowest_results


def list_filenames(directory):
    """
    Lists all filenames in a specified directory.

    :param directory: The directory to list filenames from.
    :return: List of filenames.
    """
    return [filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename))]


def start_timer(interval_seconds):
    """
    Starts a timer that displays the elapsed time in the console.

    :param interval_seconds: The interval in seconds at which to display the elapsed time.
    """
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        print(f"Timer: {elapsed_time:.2f} seconds", end="\r", flush=True)
        time.sleep(interval_seconds)
