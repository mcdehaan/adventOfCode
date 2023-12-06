import unittest

from file_reader import read_seeds_from_file, read_maps_from_file
from map_aggregator.map_aggregator import get_map_data


class TestFileReaderFunctions(unittest.TestCase):

    def test_parse_seeds(self):
        expected_result = {'seeds': [79, 14, 55, 13]}
        result = read_seeds_from_file('./test_input.txt')
        self.assertEqual(expected_result, result)

    def test_read_maps_from_file(self):
        expected_seed_to_soil_result = [
            {'destination range start': 50, 'range length': 2, 'source range start': 98},
            {'destination range start': 52, 'range length': 48, 'source range start': 50}
        ]
        expected_light_to_temp_result = [
            {'destination range start': 45, 'range length': 23, 'source range start': 77},
            {'destination range start': 81, 'range length': 19, 'source range start': 45},
            {'destination range start': 68, 'range length': 13, 'source range start': 64}
        ]

        all_maps = read_maps_from_file('./test_input.txt')
        result = get_map_data(all_maps, 'seed-to-soil map')
        self.assertEqual(expected_seed_to_soil_result, result)
        result = get_map_data(all_maps, 'light-to-temperature map')
        self.assertEqual(expected_light_to_temp_result, result)


if __name__ == '__main__':
    unittest.main()
