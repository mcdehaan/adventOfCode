import { readTextFile } from '../day1/fileReader.js';
import { parseNumberArrays } from './numberParser.js';
import { checkSequences } from './sequenceChecker.js';
import { getDampenedSequences } from './problemDampener.js';

const content = readTextFile('./testdata/actual_input.txt');
const numberArrays = parseNumberArrays(content);

console.log('Parsed number arrays:');
console.log(numberArrays);

const checkedSequences = checkSequences(numberArrays);
console.log('\nChecked sequences:', checkedSequences);

const safeSequences = checkedSequences.filter(result => result.status === 'safe');
console.log('\nSafe sequences:', safeSequences);

const unSafeSequences = checkedSequences.filter(result => result.status === 'unsafe');
console.log('\nUnsafe sequences:', unSafeSequences);

console.log('\nProblem Dampener Analysis:');
const dampenedResults = getDampenedSequences(unSafeSequences);
const dampenableSolutions = dampenedResults.filter(result => result.canBeDampened);
console.log('\nDampened sequences:', dampenableSolutions);

console.log(`\nTotal number of safe sequences: ${safeSequences.length + dampenableSolutions.length}`);
