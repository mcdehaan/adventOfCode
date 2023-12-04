import unittest
from global_types.colors_enum import Colors 
from file_interpreter import interpret_file_line, interpret_file_lines


class TestFileInterpreterFunctions(unittest.TestCase):

    def test_interpret_file_line(self):
        test_cases = [
            ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
             {1: [
                 [{Colors.BLUE.name: 3, Colors.GREEN.name: 0, Colors.RED.name: 4}],
                 [{Colors.BLUE.name: 6, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 2, Colors.RED.name: 0}]]}),
            ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
             {2: [
                 [{Colors.BLUE.name: 1, Colors.GREEN.name: 2, Colors.RED.name: 0}],
                 [{Colors.BLUE.name: 4, Colors.GREEN.name: 3, Colors.RED.name: 1}],
                 [{Colors.BLUE.name: 1, Colors.GREEN.name: 1, Colors.RED.name: 0}]]}),
            ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
             {3: [
                 [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                 [{Colors.BLUE.name: 5, Colors.GREEN.name: 13, Colors.RED.name: 4}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 5, Colors.RED.name: 1}]]}),
            ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
             {4: [
                 [{Colors.BLUE.name: 6, Colors.GREEN.name: 1, Colors.RED.name: 3}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 3, Colors.RED.name: 6}],
                 [{Colors.BLUE.name: 15, Colors.GREEN.name: 3, Colors.RED.name: 14}]]}),
            ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
             {5: [
                 [{Colors.BLUE.name: 1, Colors.GREEN.name: 3, Colors.RED.name: 6}],
                 [{Colors.BLUE.name: 2, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 0, Colors.RED.name: 0}]]})
        ]
        for input_string, expected_result in test_cases:
            result = interpret_file_line(input_string)
            self.assertEqual(expected_result, result)

    def test_interpret_file_lines(self):
        input_lines = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
        expected_result = [
            {1: [
                 [{Colors.BLUE.name: 3, Colors.GREEN.name: 0, Colors.RED.name: 4}],
                 [{Colors.BLUE.name: 6, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 2, Colors.RED.name: 0}]]},
            {2: [
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 2, Colors.RED.name: 0}],
                [{Colors.BLUE.name: 4, Colors.GREEN.name: 3, Colors.RED.name: 1}],
                [{Colors.BLUE.name: 1, Colors.GREEN.name: 1, Colors.RED.name: 0}]]},
            {3: [
                [{Colors.BLUE.name: 6, Colors.GREEN.name: 8, Colors.RED.name: 20}],
                [{Colors.BLUE.name: 5, Colors.GREEN.name: 13, Colors.RED.name: 4}],
                [{Colors.BLUE.name: 0, Colors.GREEN.name: 5, Colors.RED.name: 1}]]},
            {4: [
                 [{Colors.BLUE.name: 6, Colors.GREEN.name: 1, Colors.RED.name: 3}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 3, Colors.RED.name: 6}],
                 [{Colors.BLUE.name: 15, Colors.GREEN.name: 3, Colors.RED.name: 14}]]},
            {5: [
                 [{Colors.BLUE.name: 1, Colors.GREEN.name: 3, Colors.RED.name: 6}],
                 [{Colors.BLUE.name: 2, Colors.GREEN.name: 2, Colors.RED.name: 1}],
                 [{Colors.BLUE.name: 0, Colors.GREEN.name: 0, Colors.RED.name: 0}]]}
        ]
        result = interpret_file_lines(input_lines)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
