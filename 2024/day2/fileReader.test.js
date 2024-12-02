import { expect, test, describe } from "bun:test";
import { readTextFile } from './fileReader.js';

describe('readTextFile', () => {
    test('should correctly read test_input.txt', () => {
        const expectedContent = "7 6 4 2 1\r\n1 2 7 8 9\r\n9 7 6 2 1\r\n1 3 2 4 5\r\n8 6 4 4 1\r\n1 3 6 7 9";
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
