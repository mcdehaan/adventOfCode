import { expect, test, describe } from "bun:test";
import { sumArray } from './arraySum.js';

describe('sumArray', () => {
    test('sums array of positive numbers', () => {
        expect(sumArray([8, 25, 88, 40])).toBe(161);
    });

    test('handles empty array', () => {
        expect(sumArray([])).toBe(0);
    });

    test('handles array with single number', () => {
        expect(sumArray([42])).toBe(42);
    });

    test('handles array with negative numbers', () => {
        expect(sumArray([10, -5, 15, -20])).toBe(0);
    });
});
