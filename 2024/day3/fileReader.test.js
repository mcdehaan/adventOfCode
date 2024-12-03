import { expect, test, describe } from "bun:test";
import { readTextFile } from './fileReader.js';

describe('readTextFile', () => {
    test('should correctly read test_input.txt', () => {
        const expectedContent = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
        const content = readTextFile('./testdata/test_input.txt');
        console.log('Actual content:', content);
        console.log('Expected content:', expectedContent);
        expect(content.trim()).toBe(expectedContent);
    });

    test('should throw error for non-existent file', () => {
        expect(() => {
            readTextFile('./nonexistent.txt');
        }).toThrow('Error reading file');
    });
});
