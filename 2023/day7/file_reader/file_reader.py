def convert_hand_to_numbers(hand):
    """
    Converts characters in the hand to their respective numbers.

    :param hand: String representing a hand.
    :return: List of numbers representing the hand.
    """
    conversion = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return [conversion.get(card, int(card) if card.isdigit() else card) for card in hand]


def read_file_to_map(filename):
    """
    Reads a file and maps its content to a specific format.

    :param filename: The name of the file to read from.
    :return: A list of dictionaries with 'hand' and 'bid'.
    """
    mapped_data = []
    with open(filename, 'r') as file:
        for line in file:
            hand_str, bid_str = line.strip().split()
            hand = convert_hand_to_numbers(hand_str)
            bid = int(bid_str)
            mapped_data.append({'hand': hand, 'bid': bid})

    return mapped_data
