import { checkSequences } from './sequenceChecker.js';

function findSafetyWithOneIgnored(data) {
    const sequence = data.sequence;

    for (let i = 0; i < sequence.length; i++) {
        // Create new sequence without element at index i
        const newSequence = [...sequence.slice(0, i), ...sequence.slice(i + 1)];
        const [analysis] = checkSequences([newSequence]);
        
        if (analysis.status === 'safe') {
            return {
                canBeSafe: true,
                safeSequence: newSequence,
                ignoredValue: sequence[i],
                ignoredIndex: i
            };
        }
    }

    return {
        canBeSafe: false,
        safeSequence: null,
        ignoredValue: null,
        ignoredIndex: null
    };
}

function getDampenedSequences(sequences) {
    return sequences.map(seq => {
        const result = findSafetyWithOneIgnored(seq);
        return {
            originalSequence: seq.sequence,
            canBeDampened: result.canBeSafe,
            dampenedSequence: result.safeSequence
        };
    });
}

export { findSafetyWithOneIgnored, getDampenedSequences };
