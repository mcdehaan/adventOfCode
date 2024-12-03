import { expect, test, describe } from "bun:test";
import { findMultiplications, findMultiplicationsWithExclusions } from './mulFinder.js';

describe('findMultiplications', () => {
    test('finds single multiplication pattern', () => {
        const input = 'text mul(123,456) text';
        expect(findMultiplications(input)).toEqual(['mul(123,456)']);
    });

    test('finds multiple multiplication patterns', () => {
        const input = 'mul(1,2) some text mul(123,456) more mul(7,89)';
        expect(findMultiplications(input)).toEqual(['mul(1,2)', 'mul(123,456)', 'mul(7,89)']);
    });

    test('returns empty array when no patterns found', () => {
        const input = 'text without any multiplications';
        expect(findMultiplications(input)).toEqual([]);
    });

    test('only matches numbers up to 3 digits', () => {
        const input = 'mul(1234,56) mul(12,345) mul(123,456)';
        expect(findMultiplications(input)).toEqual(['mul(12,345)', 'mul(123,456)']);
    });

    test('handles empty string input', () => {
        expect(findMultiplications('')).toEqual([]);
    });
});

describe('findMultiplicationsWithExclusions', () => {
    test('ignores excluded multiplications', () => {
        expect(findMultiplicationsWithExclusions(`xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`)).toEqual(['mul(2,4)', 'mul(8,5)']);
    });

    test('handles complex string input', () => {
        expect(findMultiplicationsWithExclusions(`why()>mul(389,101)don't()<^}who()mul(501,691)'select()mul(551,120),]?from(545,381)?*%~mul(492,926),:(who() {$ when()mul(348,721)'?/)?!what(784,670)mul(811,483): where()why()why()>$[when()do(),~*# {/mul(312,382)`)).toEqual(['mul(389,101)', 'mul(312,382)']);
    });
});
