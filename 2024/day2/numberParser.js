import { readTextFile } from '../day1/fileReader.js';

/**
 * Parses input string content into arrays of numbers, one array per line
 * @param {string} content - String content to parse
 * @returns {number[][]} Array of arrays, where each inner array contains the numbers from one line
 */
export function parseNumberArrays(content) {
    if (!content.trim()) return [];
    
    return content
        .trim()
        .split(/\r?\n/)
        .map(line => line.trim())
        .filter(line => line.length > 0)
        .map(line => line.split(/\s+/).map(Number));
}
