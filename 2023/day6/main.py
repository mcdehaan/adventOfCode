# Part 1
from file_reader.file_reader import map_time_distance_from_file
from logic.logic import multiply_results, find_ways_to_win_race

if __name__ == '__main__':
    print('Part 1:')
    input_file_path = './input.txt'
    races = map_time_distance_from_file(input_file_path)
    nr_of_ways = []
    for race in races:
        nr_of_ways.append(find_ways_to_win_race(race['time'], race['distance']))
    final_result = multiply_results(nr_of_ways)
    print(f"Final result: {final_result}")
