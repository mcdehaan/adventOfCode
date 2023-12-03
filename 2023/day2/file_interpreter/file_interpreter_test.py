import unittest

from file_interpreter import (
    interpret_file_line, interpret_file_lines
)


class TestLogicFunctions(unittest.TestCase):

    def test_interpret_file_line(self):
        test_cases = [
            ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
             {1: [
                 [{'blue': 3, 'green': 0, 'red': 4}],
                 [{'blue': 6, 'green': 2, 'red': 1}],
                 [{'blue': 0, 'green': 2, 'red': 0}]]}),
            ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
             {2: [
                 [{'blue': 1, 'green': 2, 'red': 0}],
                 [{'blue': 4, 'green': 3, 'red': 1}],
                 [{'blue': 1, 'green': 1, 'red': 0}]]}),
            ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
             {3: [
                 [{'blue': 6, 'green': 8, 'red': 20}],
                 [{'blue': 5, 'green': 13, 'red': 4}],
                 [{'blue': 0, 'green': 5, 'red': 1}]]}),
            ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
             {4: [
                 [{'blue': 6, 'green': 1, 'red': 3}],
                 [{'blue': 0, 'green': 3, 'red': 6}],
                 [{'blue': 15, 'green': 3, 'red': 14}]]}),
            ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
             {5: [
                 [{'blue': 1, 'green': 3, 'red': 6}],
                 [{'blue': 2, 'green': 2, 'red': 1}],
                 [{'blue': 0, 'green': 0, 'red': 0}]]})
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
                 [{'blue': 3, 'green': 0, 'red': 4}],
                 [{'blue': 6, 'green': 2, 'red': 1}],
                 [{'blue': 0, 'green': 2, 'red': 0}]]},
            {2: [
                [{'blue': 1, 'green': 2, 'red': 0}],
                [{'blue': 4, 'green': 3, 'red': 1}],
                [{'blue': 1, 'green': 1, 'red': 0}]]},
            {3: [
                [{'blue': 6, 'green': 8, 'red': 20}],
                [{'blue': 5, 'green': 13, 'red': 4}],
                [{'blue': 0, 'green': 5, 'red': 1}]]},
            {4: [
                 [{'blue': 6, 'green': 1, 'red': 3}],
                 [{'blue': 0, 'green': 3, 'red': 6}],
                 [{'blue': 15, 'green': 3, 'red': 14}]]},
            {5: [
                 [{'blue': 1, 'green': 3, 'red': 6}],
                 [{'blue': 2, 'green': 2, 'red': 1}],
                 [{'blue': 0, 'green': 0, 'red': 0}]]}
        ]
        result = interpret_file_lines(input_lines)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
