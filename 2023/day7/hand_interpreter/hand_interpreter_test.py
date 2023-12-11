import unittest

from hand_interpreter import find_current_hand


class TestHandInterpreterFunctions(unittest.TestCase):
    def test_has_five_of_a_kind(self):
        expected_result = 'five_of_a_kind'
        result = find_current_hand([2, 2, 2, 2, 2])
        self.assertEqual(expected_result, result)

    def test_has_four_of_a_kind(self):
        expected_result = 'four_of_a_kind'
        result = find_current_hand([2, 2, 2, 2, 3])
        self.assertEqual(expected_result, result)

    def test_has_full_house(self):
        expected_result = 'full_house'
        result = find_current_hand([2, 2, 2, 3, 3])
        self.assertEqual(expected_result, result)

    def test_has_three_of_a_kind(self):
        expected_result = 'three_of_a_kind'
        result = find_current_hand([2, 2, 2, 1, 3])
        self.assertEqual(expected_result, result)

    def test_has_two_pairs(self):
        expected_result = 'two_pairs'
        result = find_current_hand([2, 2, 1, 3, 3])
        self.assertEqual(expected_result, result)

    def test_has_one_pair(self):
        expected_result = 'one_pair'
        result = find_current_hand([2, 2, 1, 4, 3])
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
