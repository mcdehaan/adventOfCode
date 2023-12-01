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
        print("\nThe file was not found")
        return []  # Return an empty list in case of an exception


def replace_words_with_numbers(input_lines):
    # Dictionary mapping words to numbers
    words_numbers = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }

    # Regex pattern to find number words
    pattern = r'(one|two|three|four|five|six|seven|eight|nine)'

    intermittent_result_lines = []
    final_result_lines = []

    print("\n")
    # Loop to replace each first number word
    for line in input_lines:

        # Function to do the actual replacement
        def replace_match(match):
            word = match.group(0)
            return words_numbers.get(word, word)

        # Replace the first occurrence of the pattern in the string
        result_line = re.sub(pattern, replace_match, line, count=1)
        print(f"Result line = {result_line}")

        # Put the results in a temporary list
        intermittent_result_lines.append(result_line)

    # Loop to replace each last number word
    for line in intermittent_result_lines:
        matches = list(re.finditer(pattern, line))
        if matches:
            # If there are matches, replace only the last one
            last_match = matches[-1]
            start, end = last_match.span()
            word_to_replace = last_match.group(0)
            number = words_numbers.get(word_to_replace, word_to_replace)

            result_line = line[:start] + number + line[end:]
        else:
            result_line = line  # No change if no match is found

        final_result_lines.append(result_line)

    return final_result_lines


def convert_string_to_number(input_string):
    for string in input_string:
        try:
            # Try converting to an integer
            return int(string)
        except ValueError:
            print("String to Int conversion error")
            return string


def find_first_digit(input_line):
    print("\n")
    # Use regular expression to find the first digit
    match = re.search(r'\d', input_line)
    if match:
        print(f"First digit in '{input_line}' is '{match.group()}' at position {match.start()}.")
        return convert_string_to_number(match.group())
    else:
        print(f"No digit found in '{input_line}'.")


def find_last_digit(input_line):
    # Use regular expression to find the last digit
    match = re.search(r'\d(?![\d\S]*\d)', input_line)
    if match:
        print(f"Last digit in '{input_line}' is '{match.group()}' at position {match.start()}.")
        return convert_string_to_number(match.group())
    else:
        print(f"No digit found in '{input_line}'.")


def extract_numbers(input_lines):
    digit_lines = []
    # convert words to numbers before extracting them
    converted_lines = replace_words_with_numbers(input_lines)

    for line in converted_lines:
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
