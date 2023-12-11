import unittest

from file_reader.file_reader import map_time_distance_from_file
from logic.logic import find_ways_to_win_race, multiply_results


class IntegrationTest(unittest.TestCase):

    # Part 1
    def test_full_integration_part_1(self):
        expected_result = 71503

        input_file_path = './file_reader/test_input.txt'
        races = map_time_distance_from_file(input_file_path)
        nr_of_ways = []
        for race in races:
            nr_of_ways.append(find_ways_to_win_race(race['time'], race['distance']))
        final_result = multiply_results(nr_of_ways)
        self.assertEqual(expected_result, final_result)
        print(f"Final result: {final_result}")


if __name__ == '__main__':
    unittest.main()
