from file_reader.file_reader import read_and_process_file
from logic.logic import calculate_total_score, calculate_copies, calculate_instances

# Part 1
if __name__ == '__main__':
    cards = read_and_process_file('./input.txt')
    final_result = calculate_total_score(cards)
    print(f"\nFinal result: {final_result}")

# Part 2
if __name__ == '__main__':
    cards = read_and_process_file('./input.txt')
    cards_with_copies = calculate_copies(cards)
    all_instances = calculate_instances(cards_with_copies)
    print(f"\nFinal result: \n{all_instances}")
