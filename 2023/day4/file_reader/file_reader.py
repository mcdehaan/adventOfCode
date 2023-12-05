
def read_and_process_file(file_path):
    results = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split('|')
            card_part, numbers_part = parts[0], parts[1]

            # Extract card number, assuming it's the first number after 'Card'
            card_number = int(card_part.split()[1].replace(':', ''))

            # Assuming the winning numbers are the remaining numbers in card_part
            winning_numbers = [int(num) for num in card_part.split()[2:]]
            actual_numbers = [int(num) for num in numbers_part.split()]

            # Append the processed data to results
            results.append({'card': card_number, 'winning_numbers': winning_numbers, 'actual_numbers': actual_numbers})

    return results

