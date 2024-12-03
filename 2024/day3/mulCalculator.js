function calculateMultiplications(mulArray) {
    return mulArray.map(mulStr => {
        // Extract numbers using regex
        const match = mulStr.match(/mul\((\d+),(\d+)\)/);
        if (!match) return 0;  // Return 0 for invalid format
        
        // Convert to numbers and multiply
        const num1 = parseInt(match[1], 10);
        const num2 = parseInt(match[2], 10);
        return num1 * num2;
    });
}

export { calculateMultiplications };
