/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    arr.sort((a,b) => a-b);
    let abs = Infinity;
    let ans = [];

    for (let i = 1; i < arr.length; i++) {
        abs = Math.min(abs, arr[i]-arr[i-1])
    }

    for (let i = 1; i < arr.length; i++) {
        (arr[i] - arr[i-1]) == abs ? ans.push([arr[i-1], arr[i]]) : abs = abs;
    }

    return ans;
};