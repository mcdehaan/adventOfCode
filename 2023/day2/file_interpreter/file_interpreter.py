from collections import defaultdict
from global_types.colors_enum import Colors


def interpret_file_line(line):
    game_results = []

    # Extract game number and scores
    game_number, colors_str = line.split(': ')
    game_number = int(game_number.split(' ')[-1])

    # Splitting each score segment
    color_segments = colors_str.split('; ')

    # Process each color segment
    for segment in color_segments:
        # Create a default dictionary for colors initialized to 0
        color_amounts = defaultdict(int)

        # Split and process each color-amount pair
        color_amount_pairs = segment.split(', ')
        for pair in color_amount_pairs:
            if pair:
                score, color_str = pair.split(' ')
                # Convert color string to enum if it exists in the enum, otherwise skip
                color = next((c for c in Colors if c.value == color_str), None)
                if color is not None:
                    color_amounts[color] = int(score)

        # Convert the default-dict to a list of color-score pairs
        game_results.append([{color.name: color_amounts[color] for color in Colors}])

    # Ensure each game has three items
    while len(game_results) < 3:
        game_results.append([{color.name: 0 for color in Colors}])

    return {game_number: game_results}


def interpret_file_lines(lines):
    result_lines = []

    for line in lines:
        result_line = interpret_file_line(line)
        result_lines.append(result_line)

    return result_lines
