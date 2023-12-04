from file_reader.file_reader import read_file
from file_interpreter.file_interpreter import interpret_file_lines
from global_types.colors_enum import Colors
from logic.game_logic import verify_results, extract_round_numbers, add_round_numbers, calculate_total_game_power

# Part 1
if __name__ == '__main__':
    lines = read_file('./input.txt')
    games = interpret_file_lines(lines)
    valid_games = verify_results(games, {
        Colors.RED.name: 12, Colors.GREEN.name: 13, Colors.BLUE.name: 14
    })
    round_numbers = extract_round_numbers(valid_games)
    final_result = add_round_numbers(round_numbers)
    print(f"\nFinal result part 1 = {final_result}")

# Part 2
if __name__ == '__main__':
    lines = read_file('./input.txt')
    games = interpret_file_lines(lines)
    final_result = calculate_total_game_power(games)
    print(f"\nFinal result part 2 = {final_result}")

