import { readTextFile } from './fileReader.js';
import { parseNumberPairs, sortArrayPairs, calculateDifferences, sumArray } from './numberParser.js';

const content = readTextFile('./testdata/actual_input.txt');
const [firstNumbers, secondNumbers] = parseNumberPairs(content);

console.log('Original first numbers:', firstNumbers);
console.log('Original second numbers:', secondNumbers);

const [sortedFirst, sortedSecond] = sortArrayPairs(firstNumbers, secondNumbers);
console.log('\nSorted first numbers:', sortedFirst);
console.log('Sorted second numbers:', sortedSecond);

const differences = calculateDifferences(sortedFirst, sortedSecond);
console.log('\nDifferences (second - first):', differences);

const total = sumArray(differences);
console.log('Sum of differences:', total);
