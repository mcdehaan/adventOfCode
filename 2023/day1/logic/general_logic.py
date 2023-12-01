import re

from logic.number_word_logic import replace_first_word_with_number, replace_last_word_with_number


def read_file_lines(path):
    try:
        with open(path, 'r') as file:
            lines = []
            for line in file:
                # Append each line to the list
                lines.append(line.strip())

        return lines

    except FileNotFoundError:
        print("\nThe file was not found")
        return []  # Return an empty list in case of an exception


def convert_string_to_number(input_string):
    for string in input_string:
        try:
            # Try converting to an integer
            return int(string)
        except ValueError:
            print("String to Int conversion error")
            return string


def find_first_digit(input_line):
    # Convert the first word number to actual number
    converted_line = replace_first_word_with_number(input_line)

    # Use regular expression to find the first digit
    match = re.search(r'\d', converted_line)
    if match:
        return convert_string_to_number(match.group())
    else:
        print(f"No digit found in '{converted_line}'.")


def find_last_digit(input_line):
    # Convert the last word number to actual number
    converted_line = replace_last_word_with_number(input_line)

    # Use regular expression to find the last digit
    match = re.search(r'\d(?![\d\S]*\d)', converted_line)
    if match:
        return convert_string_to_number(match.group())
    else:
        print(f"No digit found in '{converted_line}'.")


def extract_numbers(input_lines):
    digit_lines = []
    # convert words to numbers before extracting them

    for line in input_lines:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        both_digits = first_digit * 10 + last_digit
        digit_lines.append(both_digits)

    return digit_lines


def add_all_numbers(input_numbers):
    total = 0
    for number in input_numbers:
        total = total + number
    return total
