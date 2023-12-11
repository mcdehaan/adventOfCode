import unittest

from file_reader.file_reader import read_file_to_map
from logic.logic import calculate_hand_order, calculate_score


class IntegrationTest(unittest.TestCase):

    # Part 1
    def test_full_integration_part_1(self):
        expected_result = 6440

        input_file_path = './file_reader/test_input.txt'
        game = read_file_to_map(input_file_path)
        hand_order = calculate_hand_order(game)
        print(f"\nHand order: {hand_order}")
        final_score = calculate_score(hand_order)
        self.assertEqual(expected_result, final_score)


if __name__ == '__main__':
    unittest.main()
