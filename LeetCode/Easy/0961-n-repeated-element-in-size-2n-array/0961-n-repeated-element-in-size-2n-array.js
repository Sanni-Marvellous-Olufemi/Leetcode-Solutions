/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    let hashmap = {};

    for (let i = 0; i < nums.length; i++) {
        if (!(nums[i] in hashmap)) {
            hashmap[nums[i]] = 0;
        }
        hashmap[nums[i]]++;
        
        if (hashmap[nums[i]] == (nums.length/2)) {
            return nums[i]
        }
    }
};