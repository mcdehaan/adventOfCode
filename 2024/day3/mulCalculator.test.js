import { expect, test, describe } from "bun:test";
import { calculateMultiplications } from './mulCalculator.js';

describe('calculateMultiplications', () => {
    test('calculates single multiplication correctly', () => {
        expect(calculateMultiplications(['mul(2,4)'])).toEqual([8]);
    });

    test('calculates multiple multiplications correctly', () => {
        const input = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)'];
        const expected = [8, 25, 88, 40];
        expect(calculateMultiplications(input)).toEqual(expected);
    });

    test('handles empty array', () => {
        expect(calculateMultiplications([])).toEqual([]);
    });

    test('handles invalid format', () => {
        const input = ['mul(2,4)', 'invalid', 'mul(5,5)'];
        expect(calculateMultiplications(input)).toEqual([8, 0, 25]);
    });

    test('handles large numbers', () => {
        expect(calculateMultiplications(['mul(999,999)'])).toEqual([998001]);
    });
});
