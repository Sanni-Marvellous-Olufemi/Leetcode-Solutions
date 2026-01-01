/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let n = digits.length - 1;

    while (digits[n] == 9 & n > 0){
        digits[n] = 0;
        n -= 1;
    }

    if (n == 0 & digits[n] == 9){
        digits[n] = 1;
        digits.push(0);
        return digits;
    }

    digits[n] ++;
    return digits;
    
};