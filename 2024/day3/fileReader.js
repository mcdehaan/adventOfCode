import { readFileSync } from 'fs';

/**
 * Reads the contents of a text file
 * @param {string} filePath - Path to the text file
 * @returns {string} Contents of the file
 */
export function readTextFile(filePath) {
    try {
        return readFileSync(filePath, 'utf8');
    } catch (error) {
        throw new Error(`Error reading file: ${error.message}`);
    }
}
