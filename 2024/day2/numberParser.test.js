import { expect, test, describe } from "bun:test";
import { parseNumberArrays } from './numberParser.js';

describe('parseNumberArrays', () => {
    test('should parse single line of numbers', () => {
        const input = '1 2 3 4 5';
        const expected = [[1, 2, 3, 4, 5]];
        expect(parseNumberArrays(input)).toEqual(expected);
    });

    test('should parse multiple lines of numbers', () => {
        const input = '1 2 3\n4 5 6\n7 8 9';
        const expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
        expect(parseNumberArrays(input)).toEqual(expected);
    });

    test('should handle empty lines', () => {
        const input = '1 2 3\n\n4 5 6';
        const expected = [[1, 2, 3], [4, 5, 6]];
        expect(parseNumberArrays(input)).toEqual(expected);
    });

    test('should handle varying number of values per line', () => {
        const input = '1 2\n3 4 5\n6';
        const expected = [[1, 2], [3, 4, 5], [6]];
        expect(parseNumberArrays(input)).toEqual(expected);
    });

    test('should handle extra whitespace', () => {
        const input = '  1   2   3  \n  4   5   6  ';
        const expected = [[1, 2, 3], [4, 5, 6]];
        expect(parseNumberArrays(input)).toEqual(expected);
    });

    test('should return empty array for empty input', () => {
        const input = '';
        const expected = [];
        expect(parseNumberArrays(input)).toEqual(expected);
    });
});
