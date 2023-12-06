import unittest

from file_reader.file_reader import read_maps_from_file, read_seeds_from_file, read_seed_ranges_from_file
from logic.logic import find_lowest_number
from map_aggregator.map_aggregator import list_all_seeds, iterate_seeds_trough_maps


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

    # Part 2
    def test_full_integration_part_2(self):
        expected_result = 46

        input_file_path = './file_reader/test_input.txt'
        seeds = read_seed_ranges_from_file(input_file_path)
        all_maps = read_maps_from_file(input_file_path)
        all_seeds = list_all_seeds(seeds)
        print(f"\nAll seeds: {all_seeds}")
        processed_seeds = iterate_seeds_trough_maps(all_maps, all_seeds)
        final_result = find_lowest_number(processed_seeds)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)


if __name__ == '__main__':
    unittest.main()
