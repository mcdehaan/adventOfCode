import { readTextFile } from './fileReader.js';
import { parseNumberArrays } from './numberParser.js';
import { checkSequences } from './sequenceChecker.js';

const content = readTextFile('./testdata/actual_input.txt');
const numberArrays = parseNumberArrays(content);

console.log('Parsed number arrays:');
console.log(numberArrays);

const checkedSequences = checkSequences(numberArrays);
console.log('\nChecked sequences:', checkedSequences);

const safeSequences = checkedSequences.filter(result => result.status === 'safe');
console.log('\nSafe sequences:', safeSequences);

const safeCount = safeSequences.length;
console.log(`\nTotal number of safe sequences: ${safeCount}`);
