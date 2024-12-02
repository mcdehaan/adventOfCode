import { findSafetyWithOneIgnored } from './problemDampener.js';

describe('Problem Dampener Tests', () => {
    test('findSafetyWithOneIgnored can make non-monotonic sequence safe', () => {
        const testData = {
            sequence: [1, 3, 2, 4, 5],
            status: "unsafe",
            monotonic: false,
            smallDiffs: true
        };

        const result = findSafetyWithOneIgnored(testData);
        expect(result.canBeSafe).toBe(true);
        expect(result.safeSequence).toEqual([1, 2, 4, 5]);  // First safe sequence found
        expect(result.ignoredValue).toBe(3);
        expect(result.ignoredIndex).toBe(1);
    });

    test('findSafetyWithOneIgnored can make sequence safe by removing duplicate', () => {
        const testData = {
            sequence: [8, 6, 4, 4, 1],
            status: "unsafe",
            monotonic: false,
            smallDiffs: true
        };

        const result = findSafetyWithOneIgnored(testData);
        expect(result.canBeSafe).toBe(true);
        expect(result.safeSequence).toEqual([8, 6, 4, 1]);  // First safe sequence found
        expect(result.ignoredValue).toBe(4);
        expect(result.ignoredIndex).toBe(2);
    });

    test('findSafetyWithOneIgnored handles sequences that cannot be made safe', () => {
        const testData = {
            sequence: [1, 5, 2, 6, 3],
            status: "unsafe",
            monotonic: false,
            smallDiffs: false
        };

        const result = findSafetyWithOneIgnored(testData);
        expect(result.canBeSafe).toBe(false);
        expect(result.safeSequence).toBeNull();
        expect(result.ignoredValue).toBeNull();
        expect(result.ignoredIndex).toBeNull();
    });
});
