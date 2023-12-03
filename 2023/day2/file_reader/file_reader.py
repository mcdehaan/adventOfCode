import re

from logic.number_word_logic import replace_first_word_with_number, replace_last_word_with_number


def read_file(path):
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

