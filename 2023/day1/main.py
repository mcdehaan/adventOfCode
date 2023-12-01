from logic.general_logic import read_file_lines, extract_numbers, add_all_numbers

if __name__ == '__main__':
    lines = read_file_lines('./logic/test_input.txt')
    print(f"\nAll lines = {lines}")
    numbers = extract_numbers(lines)
    print(f"\nAll numbers = {numbers}")
    result = add_all_numbers(numbers)
    print(f"\nTotal number = {result}")
