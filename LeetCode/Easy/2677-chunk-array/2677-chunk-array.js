/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let count = 1, j = -1;
    let ans = [];

    for (i of arr){
        if (count == 1){
            ans.push([]);
            j++;
        }

        ans[j].push(i);
        count == size? count = 1 : count ++;

    }
    return ans;
};
