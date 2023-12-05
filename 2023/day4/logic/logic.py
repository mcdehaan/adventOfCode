def count_duplicate_numbers(array1, array2):
    """
    Counts the number of duplicate numbers between two arrays.

    This function converts the arrays to sets and finds their intersection,
    which represents the common elements (duplicates) between the two arrays.
    It then returns the count of these duplicate numbers.

    :param array1: First array of integers.
    :param array2: Second array of integers.
    :return: The number of duplicate numbers between the two arrays.
    """
    # Convert arrays to sets and find intersection
    set1 = set(array1)
    set2 = set(array2)
    common_elements = set1.intersection(set2)

    # Return the count of duplicate numbers
    return len(common_elements)


def calculate_score(winning_numbers_amount):
    """
    Calculates the score based on the number of winning numbers.

    This function calculates the score based on the number of winning numbers and returns it.

    :param winning_numbers_amount: integer.
    :return: The score based on the amount of winning numbers.
    """
    # Calculate score based on the number of winning numbers
    score = 0
    if winning_numbers_amount > 0:
        score += 1
        for i in range(winning_numbers_amount - 1):
            score *= 2

    # Return the score
    return score


def calculate_total_score(input_cards):
    """
    Calculates the total score of all the cards.

    This function calculates the total score of all the cards and returns it.

    :param input_cards: List of dictionaries.
    :return: The total score of all the cards as int.
    """

    total_score = 0
    for card in input_cards:
        score = calculate_score(count_duplicate_numbers(card['winning_numbers'], card['actual_numbers']))
        total_score += score

    return total_score


def calculate_copies(input_cards):
    """
    Calculates the copies of cards won.

    This function calculates the rewarded copies cards and returns it in the dictionary.

    :param input_cards: List of dictionaries.
    :return: The rewarded copies cards as list of dictionaries.
    """
    return_cards = []
    for input_card in input_cards:

        card_number = input_card['card']
        winning_numbers = input_card['winning_numbers']
        actual_numbers = input_card['actual_numbers']

        duplicate_numbers_amount = count_duplicate_numbers(winning_numbers, actual_numbers)
        copies_list = []

        for i in range(duplicate_numbers_amount):
            copies_list.append(card_number + i + 1)

        return_card = {
            'card': card_number,
            'winning_numbers': winning_numbers,
            'actual_numbers': actual_numbers,
            'copies': copies_list
        }

        return_cards.append(return_card)

    return return_cards


def calculate_instances(input_cards):
    """
    Calculates the instances of each card.

    This function calculates the instances of each card and returns it in the dictionary.

    :param input_cards: List of dictionaries.
    :return: The total number of all cards and copies.
    """

    return_cards = []
    all_copies = []
    for input_card in input_cards:
        for copy in input_card['copies']:
            all_copies.append(copy)
    print(f"\nAll copies: {sorted(all_copies)}")

    sorted_input_cards = sorted(input_cards, key=lambda k: k['card'])

    for input_card in sorted_input_cards:

        card_number = input_card['card']
        winning_numbers = input_card['winning_numbers']
        actual_numbers = input_card['actual_numbers']
        copies_list = input_card['copies']

        instances = 1

        for copy in all_copies:
            if copy == card_number:
                instances += 1

        if instances > 1:
            multiplied_copies = copies_list * (instances - 1)
            for copy in multiplied_copies:
                all_copies.append(copy)

        print(f"\nAll Copies: {all_copies}")

        return_card = {
            'card': card_number,
            'winning_numbers': winning_numbers,
            'actual_numbers': actual_numbers,
            'copies': copies_list,
            'instances': instances
        }

        return_cards.append(return_card)
        print(f"\nreturn_card: \n{return_card}")

    all_cards = len(input_cards) + len(all_copies)

    return all_cards
