import re


def read_file_lines(path):
    try:
        with open(path, 'r') as file:
            lines = []
            for line in file:
                # Append each line to the list
                lines.append(line.strip())

        return lines

    except FileNotFoundError:
        print("The file was not found")
        return []  # Return an empty list in case of an exception


def extract_numbers(input_lines):
    digit_lines = []

    def convert_to_number(input_string):
        for string in input_string:
            try:
                # Try converting to an integer
                return int(string)
            except ValueError:
                print("String to Int Conversion Error")
                return string

    def find_first_digit(input_line):
        print("\n")
        # Use regular expression to find the first digit
        match = re.search(r'\d', input_line)
        if match:
            print(f"First digit in '{input_line}' is '{match.group()}' at position {match.start()}.")
            return convert_to_number(match.group())
        else:
            print(f"No digit found in '{input_line}'.")

    def find_last_digit(input_line):
        # Use regular expression to find the first digit
        match = re.search(r'\d(?![\d\S]*\d)', input_line)
        if match:
            print(f"Last digit in '{input_line}' is '{match.group()}' at position {match.start()}.")
            return convert_to_number(match.group())
        else:
            print(f"No digit found in '{input_line}'.")

    for line in input_lines:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        both_digits = first_digit*10 + last_digit
        digit_lines.append(both_digits)

    print(f"\nDigit lines: {digit_lines}")
    return digit_lines


def add_all_numbers(input_numbers):
    total = 0
    for number in input_numbers:
        total = total + number
    return total
