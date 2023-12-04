class NumberWithCoordinates:
    def __init__(self):
        self.numbers = {}  # Format: { 'number': [(row1, col1), (row2, col2), ...] }

    def add_digit(self, number, coordinates):
        if number not in self.numbers:
            self.numbers[number] = []
        self.numbers[number].append(coordinates)

    def __repr__(self):
        return str(self.numbers)

