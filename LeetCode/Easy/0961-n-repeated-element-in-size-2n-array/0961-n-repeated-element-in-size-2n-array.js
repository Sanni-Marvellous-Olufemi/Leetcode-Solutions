/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    let hashmap = new Map;

    for (let i = 0; i < nums.length; i++) {
        hashmap.set(nums[i], (hashmap.get(nums[i]) ?? 0) + 1);
        
        if (hashmap.get(nums[i]) == (nums.length/2)) {
            return nums[i]
        }
    }
};