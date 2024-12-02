/**
 * Checks if a sequence of numbers is strictly increasing or decreasing
 * @param {number[]} numbers - Array of numbers to check
 * @returns {boolean} True if sequence is strictly increasing or decreasing
 */
function isStrictSequence(numbers) {
    if (numbers.length <= 1) return true;
    
    let increasing = true;
    let decreasing = true;
    
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] <= numbers[i-1]) {
            increasing = false;
        }
        if (numbers[i] >= numbers[i-1]) {
            decreasing = false;
        }
    }
    
    return increasing || decreasing;
}

/**
 * Checks if consecutive numbers in a sequence have differences no greater than 3
 * @param {number[]} numbers - Array of numbers to check
 * @returns {boolean} True if all consecutive differences are <= 3
 */
function hasSmallDifferences(numbers) {
    if (numbers.length <= 1) return true;
    
    for (let i = 1; i < numbers.length; i++) {
        if (Math.abs(numbers[i] - numbers[i-1]) > 3) {
            return false;
        }
    }
    
    return true;
}

/**
 * Checks arrays of numbers and marks them as safe or unsafe based on both monotonicity and differences
 * @param {number[][]} arrayOfArrays - Array containing arrays of numbers to check
 * @returns {Array<{sequence: number[], status: string, monotonic: boolean, smallDiffs: boolean}>} Array of objects containing the original sequence and its safety status
 */
export function checkSequences(arrayOfArrays) {
    return arrayOfArrays.map(sequence => {
        const monotonic = isStrictSequence(sequence);
        const smallDiffs = hasSmallDifferences(sequence);
        return {
            sequence,
            status: (monotonic && smallDiffs) ? 'safe' : 'unsafe',
            monotonic,
            smallDiffs
        };
    });
}
