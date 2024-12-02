/**
 * Parses a string containing pairs of numbers and returns two arrays
 * @param {string} content - String containing pairs of numbers separated by whitespace
 * @returns {[number[], number[]]} A tuple of two arrays containing the first and second numbers from each line
 */
export function parseNumberPairs(content) {
    const lines = content.trim().split(/\r?\n/);
    const firstNumbers = [];
    const secondNumbers = [];

    lines.forEach(line => {
        const [first, second] = line.trim().split(/\s+/).map(Number);
        firstNumbers.push(first);
        secondNumbers.push(second);
    });

    return [firstNumbers, secondNumbers];
}

/**
 * Sorts two arrays in ascending order
 * @param {number[]} firstArray - First array of numbers
 * @param {number[]} secondArray - Second array of numbers
 * @returns {[number[], number[]]} Tuple of sorted arrays
 */
export function sortArrayPairs(firstArray, secondArray) {
    return [
        [...firstArray].sort((a, b) => a - b),
        [...secondArray].sort((a, b) => a - b)
    ];
}

/**
 * Calculates the difference between corresponding elements in two arrays
 * @param {number[]} firstArray - First array of numbers
 * @param {number[]} secondArray - Second array of numbers
 * @returns {number[]} Array of absolute differences between corresponding elements
 * @throws {Error} If arrays have different lengths
 */
export function calculateDifferences(firstArray, secondArray) {
    if (firstArray.length !== secondArray.length) {
        throw new Error('Arrays must have the same length');
    }
    
    return firstArray.map((num, index) => Math.abs(secondArray[index] - num));
}

/**
 * Calculates the sum of all numbers in an array
 * @param {number[]} array - Array of numbers to sum
 * @returns {number} Sum of all numbers in the array
 */
export function sumArray(array) {
    return array.reduce((sum, num) => sum + num, 0);
}

/**
 * Counts occurrences of numbers in the second array for each number in the first array
 * @param {number[]} firstArray - First array of numbers
 * @param {number[]} secondArray - Second array of numbers
 * @returns {Array<{number: number, count: number}>} Array of objects containing each number from first array and its count in second array
 */
export function countOccurrences(firstArray, secondArray) {
    const secondArrayCounts = new Map();
    secondArray.forEach(num => {
        secondArrayCounts.set(num, (secondArrayCounts.get(num) || 0) + 1);
    });
    
    // For each number in the first array, get its count from the second array
    return firstArray.map(num => ({
        number: num,
        count: secondArrayCounts.get(num) || 0
    }));
}

/**
 * Filters arrays to only include numbers that appear in both arrays
 * @param {number[]} firstArray - First array of numbers
 * @param {number[]} secondArray - Second array of numbers
 * @returns {[number[], number[]]} Arrays filtered to only include common numbers
 */
export function filterCommonNumbers(firstArray, secondArray) {
    const firstSet = new Set(firstArray);
    const secondSet = new Set(secondArray);
    const commonNumbers = [...firstSet].filter(num => secondSet.has(num));
    
    return [
        firstArray.filter(num => commonNumbers.includes(num)),
        secondArray.filter(num => commonNumbers.includes(num))
    ];
}

/**
 * Multiplies each number by its count from the frequency counts array
 * @param {Array<{number: number, count: number}>} frequencyCounts - Array of objects containing numbers and their counts
 * @returns {number[]} Array of numbers multiplied by their counts
 */
export function multiplyByCount(frequencyCounts) {
    return frequencyCounts.map(({number, count}) => number * count);
}
