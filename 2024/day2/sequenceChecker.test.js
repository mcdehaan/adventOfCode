import { expect, test, describe } from "bun:test";
import { checkSequences } from './sequenceChecker.js';

describe('checkSequences', () => {
    test('should mark sequence as safe when both conditions are met', () => {
        const input = [[1, 2, 3]];
        const expected = [{
            sequence: [1, 2, 3],
            status: 'safe',
            monotonic: true,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should mark sequence as unsafe when not monotonic but has small differences', () => {
        const input = [[1, 3, 2]];
        const expected = [{
            sequence: [1, 3, 2],
            status: 'unsafe',
            monotonic: false,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should mark sequence as unsafe when monotonic but has large differences', () => {
        const input = [[1, 5, 9]];  // differences of 4
        const expected = [{
            sequence: [1, 5, 9],
            status: 'unsafe',
            monotonic: true,
            smallDiffs: false
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should mark sequence as unsafe when neither condition is met', () => {
        const input = [[1, 6, 2]];  // non-monotonic and difference > 3
        const expected = [{
            sequence: [1, 6, 2],
            status: 'unsafe',
            monotonic: false,
            smallDiffs: false
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should handle multiple sequences', () => {
        const input = [
            [1, 2, 3],    // safe (both conditions met)
            [1, 5, 9],    // unsafe (differences > 3)
            [1, 3, 2]     // unsafe (not monotonic)
        ];
        const expected = [
            { sequence: [1, 2, 3], status: 'safe', monotonic: true, smallDiffs: true },
            { sequence: [1, 5, 9], status: 'unsafe', monotonic: true, smallDiffs: false },
            { sequence: [1, 3, 2], status: 'unsafe', monotonic: false, smallDiffs: true }
        ];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should handle sequences with differences exactly 3 as safe', () => {
        const input = [[1, 4, 7, 10]];  // differences of 3 (safe)
        const expected = [{
            sequence: [1, 4, 7, 10],
            status: 'safe',
            monotonic: true,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should handle single number sequences', () => {
        const input = [[1]];
        const expected = [{
            sequence: [1],
            status: 'safe',
            monotonic: true,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should handle empty sequences', () => {
        const input = [[]];
        const expected = [{
            sequence: [],
            status: 'safe',
            monotonic: true,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });

    test('should handle sequences with equal numbers as unsafe', () => {
        const input = [[1, 2, 2, 3]];
        const expected = [{
            sequence: [1, 2, 2, 3],
            status: 'unsafe',
            monotonic: false,
            smallDiffs: true
        }];
        expect(checkSequences(input)).toEqual(expected);
    });
});
