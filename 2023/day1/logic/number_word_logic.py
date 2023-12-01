import re

# Dictionary mapping words to numbers
words_numbers = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9"
}

# Regex pattern to find number words
pattern = r'(one|two|three|four|five|six|seven|eight|nine)'


# Replace word with number in string
def replace_match(match):
    word = match.group(0)
    return words_numbers.get(word, word)


def replace_first_word_with_number(input_line):
    # Replace the first occurrence of the pattern in the string
    result_line = re.sub(pattern, replace_match, input_line, count=1)

    # Return the line
    return result_line


def replace_last_word_with_number(input_line):
    last_match = None
    last_match_index = -1

    # Iterate through the string to find the last occurrence of any number word
    for i in range(len(input_line)):
        for word in words_numbers.keys():
            if input_line.startswith(word, i):
                last_match = word
                last_match_index = i

    # If a match was found, replace the last occurrence
    if last_match is not None:
        number = words_numbers[last_match]
        before = input_line[:last_match_index]
        after = input_line[last_match_index + len(last_match):]
        result_line = before + number + after
    else:
        result_line = input_line

    return result_line
