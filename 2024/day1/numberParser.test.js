import { expect, test, describe } from "bun:test";
import { parseNumberPairs, sortArrayPairs, calculateDifferences, sumArray, countOccurrences, filterCommonNumbers } from './numberParser.js';

describe('parseNumberPairs', () => {
    test('should correctly parse number pairs from input', () => {
        const input = "3   4\r\n4   3\r\n2   5\r\n1   3\r\n3   9\r\n3   3";
        const [firstNumbers, secondNumbers] = parseNumberPairs(input);
        
        expect(firstNumbers).toEqual([3, 4, 2, 1, 3, 3]);
        expect(secondNumbers).toEqual([4, 3, 5, 3, 9, 3]);
    });

    test('should handle different whitespace amounts', () => {
        const input = "3 4\r\n4    3";
        const [firstNumbers, secondNumbers] = parseNumberPairs(input);
        
        expect(firstNumbers).toEqual([3, 4]);
        expect(secondNumbers).toEqual([4, 3]);
    });
});

describe('sortArrayPairs', () => {
    test('should sort both arrays in ascending order', () => {
        const firstArray = [3, 4, 2, 1, 3, 3];
        const secondArray = [4, 3, 5, 3, 9, 3];
        const [sortedFirst, sortedSecond] = sortArrayPairs(firstArray, secondArray);
        
        expect(sortedFirst).toEqual([1, 2, 3, 3, 3, 4]);
        expect(sortedSecond).toEqual([3, 3, 3, 4, 5, 9]);
    });

    test('should not modify original arrays', () => {
        const firstArray = [3, 1, 2];
        const secondArray = [6, 4, 5];
        const originalFirst = [...firstArray];
        const originalSecond = [...secondArray];
        
        sortArrayPairs(firstArray, secondArray);
        
        expect(firstArray).toEqual(originalFirst);
        expect(secondArray).toEqual(originalSecond);
    });
});

describe('calculateDifferences', () => {
    test('should calculate absolute differences between corresponding elements', () => {
        const firstArray = [1, 2, 3, 3, 3, 4];
        const secondArray = [3, 3, 3, 4, 5, 9];
        const differences = calculateDifferences(firstArray, secondArray);
        
        expect(differences).toEqual([2, 1, 0, 1, 2, 5]);
    });

    test('should return positive differences when first number is larger', () => {
        const firstArray = [5, 3, 1];
        const secondArray = [2, 1, 0];
        const differences = calculateDifferences(firstArray, secondArray);
        
        expect(differences).toEqual([3, 2, 1]);
    });

    test('should throw error for arrays of different lengths', () => {
        const firstArray = [1, 2, 3];
        const secondArray = [4, 5];
        
        expect(() => {
            calculateDifferences(firstArray, secondArray);
        }).toThrow('Arrays must have the same length');
    });
});

describe('sumArray', () => {
    test('should sum all numbers in array', () => {
        const array = [2, 1, 0, 1, 2, 5];
        const sum = sumArray(array);
        expect(sum).toBe(11);
    });

    test('should handle negative numbers', () => {
        const array = [-3, -2, -1, 0, 1, 2];
        const sum = sumArray(array);
        expect(sum).toBe(-3);
    });

    test('should return 0 for empty array', () => {
        const array = [];
        const sum = sumArray(array);
        expect(sum).toBe(0);
    });
});

describe('countOccurrences', () => {
    test('should count occurrences of each number', () => {
        const array = [1, 2, 3, 3, 3, 4];
        const counts = countOccurrences(array);
        expect(counts).toEqual([
            { number: 1, count: 1 },
            { number: 2, count: 1 },
            { number: 3, count: 3 },
            { number: 4, count: 1 }
        ]);
    });

    test('should handle empty array', () => {
        const array = [];
        const counts = countOccurrences(array);
        expect(counts).toEqual([]);
    });

    test('should handle array with single number repeated', () => {
        const array = [5, 5, 5];
        const counts = countOccurrences(array);
        expect(counts).toEqual([
            { number: 5, count: 3 }
        ]);
    });
});

describe('filterCommonNumbers', () => {
    test('should keep only numbers that appear in both arrays', () => {
        const firstArray = [1, 2, 3, 3, 3, 4];
        const secondArray = [3, 3, 3, 4, 5, 9];
        const [filteredFirst, filteredSecond] = filterCommonNumbers(firstArray, secondArray);
        
        expect(filteredFirst).toEqual([3, 3, 3, 4]);
        expect(filteredSecond).toEqual([3, 3, 3, 4]);
    });

    test('should handle arrays with no common numbers', () => {
        const firstArray = [1, 2];
        const secondArray = [3, 4];
        const [filteredFirst, filteredSecond] = filterCommonNumbers(firstArray, secondArray);
        
        expect(filteredFirst).toEqual([]);
        expect(filteredSecond).toEqual([]);
    });

    test('should handle empty arrays', () => {
        const firstArray = [];
        const secondArray = [1, 2, 3];
        const [filteredFirst, filteredSecond] = filterCommonNumbers(firstArray, secondArray);
        
        expect(filteredFirst).toEqual([]);
        expect(filteredSecond).toEqual([]);
    });
});
