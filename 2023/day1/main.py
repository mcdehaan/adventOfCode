from logic.logic import read_file_lines, extract_numbers, add_all_numbers

if __name__ == '__main__':
    lines = read_file_lines('input.txt')
    numbers = extract_numbers(lines)
    result = add_all_numbers(numbers)
    print(f"\nTotal number = {result}")
