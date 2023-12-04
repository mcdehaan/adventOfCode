import unittest

from global_types.colors_enum import Colors
from logic import verify_result, verify_results, calculate_minimum_colors, calculate_game_power


class TestGameLogicFunctions(unittest.TestCase):

    def test_possible_game(self):
        game_data = {1:
            [
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 12, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 30, Colors.GREEN.name: 5, Colors.RED.name: 1}]
            ]}
        color_limits = {Colors.BLUE.name: 30, Colors.GREEN.name: 12, Colors.RED.name: 20}
        game_result = verify_result(game_data, color_limits)
        self.assertEqual(game_result, True)

    def test_impossible_game(self):
        game_data = {1:
            [
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                [{Colors.BLUE.name: 5, Colors.GREEN.name: 13, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 5, Colors.RED.name: 1}]
            ]}
        color_limits = {Colors.BLUE.name: 30, Colors.GREEN.name: 12, Colors.RED.name: 20}
        game_result = verify_result(game_data, color_limits)
        self.assertEqual(game_result, False)

    def test_possible_games(self):
        games_data = [
            {1: [
                [{Colors.BLUE.name: 3, Colors.GREEN.name: 0, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 2, Colors.RED.name: 0}]]},
            {2: [
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 2, Colors.RED.name: 0}],
                [{Colors.BLUE.name: 4, Colors.GREEN.name: 3, Colors.RED.name: 1}],
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 1, Colors.RED.name: 0}]]}
        ]
        expected_result = [
            {1: [[{'BLUE': 3, 'GREEN': 0, 'RED': 4}],
                 [{'BLUE': 6, 'GREEN': 2, 'RED': 1}],
                 [{'BLUE': 0, 'GREEN': 2, 'RED': 0}]]},
            {2: [[{'BLUE': 1, 'GREEN': 2, 'RED': 0}],
                 [{'BLUE': 4, 'GREEN': 3, 'RED': 1}],
                 [{'BLUE': 1, 'GREEN': 1, 'RED': 0}]]}
        ]
        color_limits = {Colors.BLUE.name: 30, Colors.GREEN.name: 12, Colors.RED.name: 20}
        game_result = verify_results(games_data, color_limits)
        self.assertEqual(game_result, expected_result)

    def test_impossible_games(self):
        games_data = [
            {1: [
                [{Colors.BLUE.name: 3, Colors.GREEN.name: 0, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 2, Colors.RED.name: 21}]]},
            {2: [
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 2, Colors.RED.name: 0}],
                [{Colors.BLUE.name: 4, Colors.GREEN.name: 3, Colors.RED.name: 1}],
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 1, Colors.RED.name: 0}]]}
        ]
        expected_result = [
            {2: [[{'BLUE': 1, 'GREEN': 2, 'RED': 0}],
                 [{'BLUE': 4, 'GREEN': 3, 'RED': 1}],
                 [{'BLUE': 1, 'GREEN': 1, 'RED': 0}]]}
        ]
        color_limits = {Colors.BLUE.name: 30, Colors.GREEN.name: 12, Colors.RED.name: 20}
        game_result = verify_results(games_data, color_limits)
        self.assertEqual(game_result, expected_result)

    def test_calculate_minimal_colors(self):
        game_data = {1:
            [
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                [{Colors.BLUE.name: 5, Colors.GREEN.name: 13, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 5, Colors.RED.name: 1}]
            ]}
        expected_result = {Colors.BLUE.name: 6, Colors.GREEN.name: 13, Colors.RED.name: 20}
        game_result = calculate_minimum_colors(game_data)
        self.assertEqual(expected_result, game_result)

    def test_calculate_game_power(self):
        game_data = {1:
            [
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                [{Colors.BLUE.name: 5, Colors.GREEN.name: 13, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 5, Colors.RED.name: 1}]
            ]}
        expected_result = 1560
        game_result = calculate_game_power(game_data)
        self.assertEqual(expected_result, game_result)


if __name__ == '__main__':
    unittest.main()
