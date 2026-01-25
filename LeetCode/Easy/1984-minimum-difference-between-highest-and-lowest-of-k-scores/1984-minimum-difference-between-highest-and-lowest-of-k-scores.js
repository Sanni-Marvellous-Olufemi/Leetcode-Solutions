/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    nums.sort((a,b) => a-b);
    let ans = Infinity;

    for (let i = 0, j = k-1; j < nums.length; i++, j++){
        ans = Math.min(ans, nums[j] - nums[i]);
    }

    return ans === Infinity? 0 : ans;
};