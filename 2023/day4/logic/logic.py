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
