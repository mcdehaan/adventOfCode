
def read_file_to_grid(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
