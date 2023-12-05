from file_reader.file_reader import read_and_process_file
from logic.logic import calculate_total_score

# Part 1
if __name__ == '__main__':
    cards = read_and_process_file('./input.txt')
    final_result = calculate_total_score(cards)
    print(f"\nFinal result: {final_result}")

