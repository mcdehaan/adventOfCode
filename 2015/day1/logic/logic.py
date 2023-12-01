def read_input_file(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
            print(content)
            return content

    except FileNotFoundError:
        print("The file was not found")


def calculate_floor(input_string):
    print("\n")
    print(f"The file contains {input_string.count('(')} '(' symbols.")
    print(f"The file contains {input_string.count(')')} ')' symbols.")
    difference = input_string.count('(') - input_string.count(')')
    print(f"Difference: {difference}")
    return difference
