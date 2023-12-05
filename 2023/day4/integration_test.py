import unittest

from file_reader.file_reader import read_and_process_file
from logic.logic import calculate_copies, calculate_total_score, calculate_instances


class IntegrationTest(unittest.TestCase):

    # Part 1
    def test_full_integration_part_1(self):
        expected_result = 13

        cards = read_and_process_file('./file_reader/test_input.txt')
        final_result = calculate_total_score(cards)
        print(f"\nFinal result: {final_result}")
        self.assertEqual(expected_result, final_result)

    # Part 2
    def test_full_integration_part_2(self):
        expected_result = 30

        cards = read_and_process_file('./file_reader/test_input.txt')
        cards_with_copies = calculate_copies(cards)
        all_instances = calculate_instances(cards_with_copies)
        self.assertEqual(expected_result, all_instances)


if __name__ == '__main__':
    unittest.main()
