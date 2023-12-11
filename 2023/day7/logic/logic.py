from hand_interpreter.hand_interpreter import find_current_hand


def calculate_hand_order(players):
    for i in range(0, len(players)):
        current_hand = find_current_hand(players[i]['hand'])

        if current_hand == 'five_of_a_kind':
            players[i]['score'] = 70000
        elif current_hand == 'four_of_a_kind':
            players[i]['score'] = 60000
        elif current_hand == 'full_house':
            players[i]['score'] = 50000
        elif current_hand == 'three_of_a_kind':
            players[i]['score'] = 40000
        elif current_hand == 'two_pairs':
            players[i]['score'] = 30000
        elif current_hand == 'one_pair':
            players[i]['score'] = 20000
        else:
            players[i]['score'] = 10000

    players_listed = sorted(players, key=lambda k: k['score'], reverse=True)
    reversed_list = players_listed[::-1]

    for i in range(0, len(reversed_list)):
        if i < (len(reversed_list) - 1):
            print(f"\nComparing {reversed_list[i]} with {reversed_list[i + 1]}")
            if reversed_list[i]['score'] == reversed_list[i + 1]['score']:
                print(f"\n...Scores are equal, comparing hands")
                for j in range(0, len(reversed_list[i]['hand'])):
                    if reversed_list[i]['hand'][j] > reversed_list[i + 1]['hand'][j]:
                        print(
                            f"\n......{reversed_list[i]['hand'][j]} is greater than {reversed_list[i + 1]['hand'][j]}")
                        reversed_list[i]['score'] += 1
                        break
                    elif reversed_list[i]['hand'][j] < reversed_list[i + 1]['hand'][j]:
                        print(
                            f"\n......{reversed_list[i]['hand'][j]} is less than {reversed_list[i + 1]['hand'][j]}")
                        reversed_list[i + 1]['score'] += 1
                        break
                    else:
                        print(
                            f"\n......{reversed_list[i]['hand'][j]} is equal to {reversed_list[i + 1]['hand'][j]}")

    final_list = sorted(reversed_list, key=lambda k: k['score'], reverse=False)

    return final_list


def calculate_score(players):
    total_score = 0
    for i in range(0, len(players)):
        print(f"\n{players[i]['bid']} * {i + 1} = {players[i]['bid'] * (i + 1)}")
        score = players[i]['bid'] * (i + 1)
        total_score += score

    return total_score
