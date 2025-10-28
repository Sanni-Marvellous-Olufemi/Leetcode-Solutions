/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    let pref = new Array(nums.length);
    let suff = new Array(nums.length);
    let ans = 0;
    pref[0] = nums[0];
    suff[nums.length-1] = nums[nums.length-1];

    for (let i = 1; i < nums.length; i++) {
        pref[i] = pref[i-1] + nums[i];
        suff[nums.length-i-1] = suff[nums.length-i] + nums[nums.length-i-1];
    }

    // console.log(JSON.stringify(pref), JSON.stringify(suff));

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 0) {
            if (suff[i] == pref[i]) {
                ans += 2;
            }
            if (Math.abs(suff[i] - pref[i]) == 1) {
                ans += 1
            }
        }
    }
    return ans
};