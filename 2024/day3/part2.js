import { readTextFile } from './fileReader.js';
import { findMultiplicationsWithExclusions } from './mulFinder.js';
import { calculateMultiplications } from './mulCalculator.js';
import { sumArray } from './arraySum.js';

const content = readTextFile('./testdata/actual_input.txt');
const multiplications = findMultiplicationsWithExclusions(content);
console.log('Multiplications found:', multiplications);
const results = calculateMultiplications(multiplications);
console.log('Multiplication results:', results);
const total = sumArray(results);
console.log('Total sum:', total);
