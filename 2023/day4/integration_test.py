import unittest

from file_reader.file_reader import read_and_process_file
from logic.logic import count_duplicate_numbers, calculate_total_score


class IntegrationTest(unittest.TestCase):

    # Part 1
    def test_full_integration_part_1(self):
        expected_result = 13

        cards = read_and_process_file('./file_reader/test_input.txt')
        final_result = calculate_total_score(cards)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)


if __name__ == '__main__':
    unittest.main()
