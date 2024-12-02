import { expect, test, describe } from "bun:test";
import { readTextFile } from './fileReader.js';

describe('readTextFile', () => {
    test('should correctly read test_input.txt', () => {
        const expectedContent = "3   4\r\n4   3\r\n2   5\r\n1   3\r\n3   9\r\n3   3";
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
