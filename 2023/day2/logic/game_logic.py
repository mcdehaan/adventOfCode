from global_types.colors_enum import Colors


def verify_result(input_game_data, input_color_limits):
    """
    Checks if any game in the provided game data exceeds the specified color limits.

    :param input_game_data: A dictionary containing game results.
    :param input_color_limits: A dictionary with color limits.
    :return: True if all games are within limits, False otherwise.
    """
    for game_rounds in input_game_data.values():
        for game_round in game_rounds:
            for color_result in game_round:
                for color, score in color_result.items():
                    if score > input_color_limits[color]:
                        return False
    return True


def verify_results(input_games_data, input_color_limits):
    valid_games = []

    for game_data in input_games_data:
        if verify_result(game_data, input_color_limits):
            valid_games.append(game_data)

    return valid_games


def extract_round_number(input_game_data):
    round_number = next(iter(input_game_data))
    return round_number


def extract_round_numbers(input_games_data):
    round_numbers = []

    for game_data in input_games_data:
        round_numbers.append(extract_round_number(game_data))

    return round_numbers


def add_round_numbers(input_round_numbers):
    total = 0
    for number in input_round_numbers:
        total = total + number
    return total


def calculate_minimum_colors(input_game_data):
    minimal_color_amounts = {Colors.RED.name: 0, Colors.GREEN.name: 0, Colors.BLUE.name: 0}

    for game_rounds in input_game_data.values():
        for game_round in game_rounds:
            for color_score in game_round:
                for color, score in color_score.items():
                    if score > minimal_color_amounts[color]:
                        minimal_color_amounts[color] = score

    return minimal_color_amounts


def calculate_game_power(input_game_data):
    minimum_colors = calculate_minimum_colors(input_game_data)
    power = minimum_colors[Colors.BLUE.name] * minimum_colors[Colors.RED.name] * minimum_colors[Colors.GREEN.name]

    return power


def calculate_total_game_power(input_games_data):
    total_power = 0
    for game_data in input_games_data:
        total_power += calculate_game_power(game_data)

    return total_power
