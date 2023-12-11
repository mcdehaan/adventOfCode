
def find_ways_to_win_race(max_time, top_distance):
    amount_of_ways_to_win = []
    for hold_time in range(0, max_time):
        speed = hold_time
        distance = speed * (max_time - hold_time)
        if distance > top_distance:
            amount_of_ways_to_win.append(hold_time)

    return len(amount_of_ways_to_win)


def multiply_results(results):
    return_value = 1
    for result in results:
        return_value = return_value * result

    return return_value

