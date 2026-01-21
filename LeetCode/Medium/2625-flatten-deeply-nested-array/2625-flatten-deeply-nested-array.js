/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let ans = [];

    function walk(array, level, n) {
        if (level > n) {
            ans.push(array);
            return;
        }

        for (i of array) {
            if ((typeof i) !== "number") {
                walk(i, level+1, n);
            } else {
                ans.push(i);
            }
        }
    }

    walk(arr, 0, n);
    return ans;

};