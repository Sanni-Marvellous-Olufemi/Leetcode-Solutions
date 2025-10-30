/**
 * @param {string} s
 * @param {number} maxLetters
 * @param {number} minSize
 * @param {number} maxSize
 * @return {number}
 */
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    let hashmap = {};
    let right = 0;
    let set = new Set();
    let curr = "";
    let ans = 0;

    for (let i = 0; i < s.length - minSize+1; i++) {
        right = i + minSize;
        curr = s.slice(i, right);
        set = new Set(curr);
        if (set.size > maxLetters) {
            continue;
        }
        hashmap[curr] = hashmap[curr] || 0;
        hashmap[curr] += 1;
    }

    for (let i in hashmap) {
        ans = hashmap[i] > ans ? hashmap[i] : ans;
    }

    return ans;
};