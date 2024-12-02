import { readTextFile } from './fileReader.js';
import { parseNumberPairs, sortArrayPairs, countOccurrences, filterCommonNumbers, multiplyByCount, sumArray } from './numberParser.js';

const content = readTextFile('./testdata/actual_input.txt');
const [firstNumbers, secondNumbers] = parseNumberPairs(content);

console.log('Original first numbers:', firstNumbers);
console.log('Original second numbers:', secondNumbers);

const [sortedFirst, sortedSecond] = sortArrayPairs(firstNumbers, secondNumbers);
console.log('\nSorted first numbers:', sortedFirst);
console.log('Sorted second numbers:', sortedSecond);

const [filteredFirst, filteredSecond] = filterCommonNumbers(firstNumbers, secondNumbers);
console.log('\nFiltered first numbers (common only):', filteredFirst);
console.log('Filtered second numbers (common only):', filteredSecond);

console.log('\nFrequency counts (numbers from first list with their counts in second list):');
const frequencyCounts = countOccurrences(filteredFirst, filteredSecond);
console.log(frequencyCounts);

console.log('\nNumbers multiplied by their counts:');
const multipliedNumbers = multiplyByCount(frequencyCounts);
console.log(multipliedNumbers);

const total = sumArray(multipliedNumbers);
console.log('Sum of multiplied numbers:', total);
