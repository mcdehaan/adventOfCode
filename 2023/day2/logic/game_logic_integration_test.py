import unittest

from file_interpreter.file_interpreter import interpret_file_lines
from file_reader.file_reader import read_file
from global_types.colors_enum import Colors
from game_logic import verify_results, extract_round_numbers, add_round_numbers, calculate_total_game_power


class TestGameLogicIntegration(unittest.TestCase):

    def test_possible_games(self):
        lines = read_file('./test_input.txt')
        games = interpret_file_lines(lines)
        valid_games = verify_results(games, {
            Colors.BLUE.name: 12, Colors.GREEN.name: 13, Colors.RED.name: 14
        })
        result = add_round_numbers(extract_round_numbers(valid_games))
        expected_result = 8
        self.assertEqual(expected_result, result)

    def test_total_game_power(self):
        lines = read_file('./test_input.txt')
        games = interpret_file_lines(lines)
        result = calculate_total_game_power(games)
        expected_result = 2286
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
