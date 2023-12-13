from file_reader.file_reader import read_seeds_from_file, read_maps_from_file, read_seed_ranges_from_file, \
    read_string_array_from_file, read_int_from_file, read_first_int_from_file, read_all_ints_and_find_min
from logic.logic import find_lowest_number
from map_aggregator.map_aggregator import expand_all_maps, iterate_seeds_trough_maps, list_all_seeds, \
    process_all_seed_files, run_process_seeds_files_parallel, list_filenames, start_timer, save_to_file

# Part 1
# if __name__ == '__main__':
#    input_file_path = './input.txt'
#    seeds = read_seeds_from_file(input_file_path)
#    all_maps = read_maps_from_file(input_file_path)
#    locations = iterate_seeds_trough_maps(all_maps, seeds['seeds'])
#    final_result = find_lowest_number(locations)
#    print(f"\nFinal result: {final_result}")

# Part 2 - Make seed files
# if __name__ == '__main__':
#    input_file_path = './input.txt'
#    seeds_ranges = read_seed_ranges_from_file(input_file_path)
#    list_all_seeds(seeds_ranges)

    # Part 2 - Process seed files
if __name__ == '__main__':
    # start_timer(1)
    input_file_path = './file_reader/test_input.txt'
    seed_files_path = './seed_files'
    # total_seed_files = count_files_in_folder(seed_files_path)  # 276150
    print(f"Reading seeds file list")
    file_list = list_filenames(seed_files_path)
    all_maps = read_maps_from_file(input_file_path)
    print(f"Total seeds file list: {len(file_list)}")
    lowest_results = run_process_seeds_files_parallel(269230, len(file_list), file_list, all_maps)
    current_lowest_result = read_all_ints_and_find_min('lowest_results.txt')
    print(f"Current lowest result: {current_lowest_result}")
    print(f"Lowest result found: {lowest_results}")
    if lowest_results < current_lowest_result:
        print(f"New lowest results: {lowest_results}")
        save_to_file('lowest_results.txt', lowest_results)

