from file_reader.file_reader import read_file_to_map
from logic.logic import calculate_hand_order, calculate_score

if __name__ == '__main__':
    print('Part 1:')
    input_file_path = './input.txt'
    game = read_file_to_map(input_file_path)
    hand_order = calculate_hand_order(game)
    final_score = calculate_score(hand_order)
    print(f"\nFinal score: {final_score}")