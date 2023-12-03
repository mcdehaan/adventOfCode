from file_reader.file_reader import read_file
from file_interpreter.file_interpreter import interpret_file_line


if __name__ == '__main__':
    lines = read_file('./input.txt')
    print(f"\nAll lines = {lines}")
    for line in lines:
        interpreted_line = interpret_file_line(line)
        print(interpreted_line)
