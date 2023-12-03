from file_reader.file_reader import read_file
from file_interpreter.file_interpreter import interpret_file_lines


if __name__ == '__main__':
    lines = read_file('./input.txt')
    print(f"\nAll lines = {lines}")
    interpreted_lines = interpret_file_lines(lines)
