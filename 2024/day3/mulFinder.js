function findMultiplications(inputString) {
    // Regular expression to match mul(xxx,xxx) where xxx is up to 3 digits
    const regex = /mul\((\d{1,3}),(\d{1,3})\)/g;
    
    // Find all matches and store them in an array
    const matches = [...inputString.matchAll(regex)];
    
    // Return the full matches (the entire mul(xxx,xxx) strings)
    return matches.map(match => match[0]);
}

function findMultiplicationsWithExclusions(inputString) {
    let regions = [];
    let i = 0;
    
    while (i < inputString.length) {
        const currentSlice = inputString.slice(i);
        
        if (currentSlice.startsWith("don't()")) {
            // Find the next "do()" after this position
            const doIndex = inputString.indexOf("do()", i + 6);
            if (doIndex !== -1) {
                regions.push([i, doIndex + 4]); // +4 for "do()"
                i = doIndex + 4;
            } else {
                i++;
            }
        } else {
            i++;
        }
    }
    
    // Create a string with excluded regions removed
    let result = '';
    let lastEnd = 0;
    
    for (const [start, end] of regions) {
        result += inputString.slice(lastEnd, start);
        console.log('Excluded region:', JSON.stringify(inputString.slice(start, end)));
        lastEnd = end;
    }
    result += inputString.slice(lastEnd);
    
    // Find multiplications in the cleaned string
    return findMultiplications(result);
}

export { findMultiplications, findMultiplicationsWithExclusions };
