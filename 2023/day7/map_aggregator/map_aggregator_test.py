import unittest

from file_reader.file_reader import read_maps_from_file
from map_aggregator import (
    get_map_data, create_total_converter_list, update_map_with_converter_list, source_destination_conversion)

all_maps = read_maps_from_file('../file_reader/test_input.txt')
ranges = {'ranges': [{'destination': 45, 'source': 77},
                     {'destination': 46, 'source': 78},
                     {'destination': 47, 'source': 79},
                     {'destination': 48, 'source': 80},
                     {'destination': 49, 'source': 81},
                     {'destination': 50, 'source': 82},
                     {'destination': 51, 'source': 83},
                     {'destination': 52, 'source': 84},
                     {'destination': 53, 'source': 85},
                     {'destination': 54, 'source': 86},
                     {'destination': 55, 'source': 87},
                     {'destination': 56, 'source': 88},
                     {'destination': 57, 'source': 89},
                     {'destination': 58, 'source': 90},
                     {'destination': 59, 'source': 91},
                     {'destination': 60, 'source': 92},
                     {'destination': 61, 'source': 93},
                     {'destination': 62, 'source': 94},
                     {'destination': 63, 'source': 95},
                     {'destination': 64, 'source': 96},
                     {'destination': 65, 'source': 97},
                     {'destination': 66, 'source': 98},
                     {'destination': 67, 'source': 99},
                     {'destination': 81, 'source': 45},
                     {'destination': 82, 'source': 46},
                     {'destination': 83, 'source': 47},
                     {'destination': 84, 'source': 48},
                     {'destination': 85, 'source': 49},
                     {'destination': 86, 'source': 50},
                     {'destination': 87, 'source': 51},
                     {'destination': 88, 'source': 52},
                     {'destination': 89, 'source': 53},
                     {'destination': 90, 'source': 54},
                     {'destination': 91, 'source': 55},
                     {'destination': 92, 'source': 56},
                     {'destination': 93, 'source': 57},
                     {'destination': 94, 'source': 58},
                     {'destination': 95, 'source': 59},
                     {'destination': 96, 'source': 60},
                     {'destination': 97, 'source': 61},
                     {'destination': 98, 'source': 62},
                     {'destination': 99, 'source': 63},
                     {'destination': 68, 'source': 64},
                     {'destination': 69, 'source': 65},
                     {'destination': 70, 'source': 66},
                     {'destination': 71, 'source': 67},
                     {'destination': 72, 'source': 68},
                     {'destination': 73, 'source': 69},
                     {'destination': 74, 'source': 70},
                     {'destination': 75, 'source': 71},
                     {'destination': 76, 'source': 72},
                     {'destination': 77, 'source': 73},
                     {'destination': 78, 'source': 74},
                     {'destination': 79, 'source': 75},
                     {'destination': 80, 'source': 76}]}


class TestMapAggregatorFunctions(unittest.TestCase):
    def test_get_map_data(self):
        map_entries = get_map_data(all_maps, 'light-to-temperature map')
        result = create_total_converter_list(map_entries)
        expected_result = ranges
        self.assertEqual(expected_result, result)

    def test_update_map_with_converter_list(self):
        existing_map = all_maps[0]
        map_entries = get_map_data(all_maps, 'light-to-temperature map')
        converter_list = create_total_converter_list(map_entries)
        result = update_map_with_converter_list(existing_map, converter_list)
        expected_result = ranges
        self.assertEqual(expected_result['ranges'], result['ranges'])

    def test_source_destination_conversion(self):
        existing_map = all_maps[0]
        map_entries = get_map_data(all_maps, 'seed-to-soil map')
        converter_list = create_total_converter_list(map_entries)
        expanded_map = update_map_with_converter_list(existing_map, converter_list)

        input_source_values = [79, 14, 55, 13]
        expected_results = [81, 14, 57, 13]
        results = source_destination_conversion(expanded_map, input_source_values)
        self.assertEqual(expected_results, results)


if __name__ == '__main__':
    unittest.main()
