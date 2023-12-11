import unittest

from file_reader.file_reader import (
    read_maps_from_file,
    read_seeds_from_file,
    read_seed_ranges_from_file,
    add_int_to_file,
    read_string_array_from_file,
    count_files_in_folder)
from logic.logic import find_lowest_number
from map_aggregator.map_aggregator import (
    list_all_seeds,
    iterate_seeds_trough_maps,
    save_to_file,
    process_all_seed_files,
    list_filenames,
    run_process_seeds_files_parallel,
    process_seeds_file)


class IntegrationTest(unittest.TestCase):

    # Part 1
    def test_full_integration_part_1(self):
        expected_result = 35

        input_file_path = './file_reader/test_input.txt'
        seeds = read_seeds_from_file(input_file_path)
        all_maps = read_maps_from_file(input_file_path)
        locations = iterate_seeds_trough_maps(all_maps, seeds['seeds'])
        final_result = find_lowest_number(locations)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)

    # Part 2 make seed files
    def test_full_integration_part_2_1(self):
        expected_result = 46

        input_file_path = './file_reader/test_input.txt'
        seeds = read_seed_ranges_from_file(input_file_path)
        list_all_seeds(seeds)

    # Process seed files
    def test_full_integration_part_2_2(self):
        input_file_path = './file_reader/test_input.txt'
        seed_files_path = './seed_files'
        # total_seed_files = count_files_in_folder(seed_files_path)  # 276150
        # file_list = list_filenames(seed_files_path)
        # save_to_file("file_list.txt", file_list)
        file_list = read_string_array_from_file("file_list.txt")
        all_maps = read_maps_from_file(input_file_path)
        print(f"file_list: {len(file_list)}")
        run_process_seeds_files_parallel(0, 10, file_list, all_maps, 4)
        # add_int_to_file("result.txt", lowest_seed)
        # lowest_results = process_all_seed_files(seed_files_path, all_maps)
        # final_result = find_lowest_number(lowest_results)
        # print(f"\nFinal result: {final_result}")
        # self.assertEqual(expected_result, final_result)


if __name__ == '__main__':
    unittest.main()
