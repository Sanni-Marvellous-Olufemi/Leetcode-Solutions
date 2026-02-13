/**
 * @param {string} s
 * @return {number}
 */
var longestBalanced = function (s) {
    let ans = 0;

    for (let i = 0; i < s.length; i++) {
        let hashmap = {};

        for (let j = i; j < s.length; j++) {
            hashmap[s[j]] = hashmap[s[j]] ? hashmap[s[j]] + 1 : 1;
            ans = check(hashmap, hashmap[s[j]]) ? Math.max(ans, j - i + 1) : ans
        }
    }

    function check(obj, curr) {
        for (let k of Object.values(obj)) {
            if (k != curr) {
                return false;
            };
        };
        return true;
    };

    return ans;
};