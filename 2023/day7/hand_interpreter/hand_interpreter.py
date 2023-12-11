from collections import Counter


def has_five_of_a_kind(hand):
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return True

    return False


def has_four_of_a_kind(hand):
    value_counts = Counter(hand)
    return any(count == 4 for count in value_counts.values())


def has_full_house(hand):
    value_counts = Counter(hand)
    if len(value_counts) != 2:
        return False

    counts = list(value_counts.values())
    return sorted(counts) == [2, 3]


def has_three_of_a_kind(hand):
    value_counts = Counter(hand)
    return any(count == 3 for count in value_counts.values())


def has_two_pairs(hand):
    value_counts = Counter(hand)
    if len(value_counts) != 3:
        return False

    counts = list(value_counts.values())
    return counts.count(2) == 2 and counts.count(1) == 1


def has_one_pair(hand):
    value_counts = Counter(hand)
    return 2 in value_counts.values() and len(value_counts) == 4


def find_current_hand(hand):
    if has_five_of_a_kind(hand):
        current_hand = 'five_of_a_kind'
    elif has_four_of_a_kind(hand):
        current_hand = 'four_of_a_kind'
    elif has_full_house(hand):
        current_hand = 'full_house'
    elif has_three_of_a_kind(hand):
        current_hand = 'three_of_a_kind'
    elif has_two_pairs(hand):
        current_hand = 'two_pairs'
    elif has_one_pair(hand):
        current_hand = 'one_pair'
    else:
        current_hand = 'high_card'

    return current_hand


def multiply_results(results):
    return_value = 1
    for result in results:
        return_value = return_value * result

    return return_value

