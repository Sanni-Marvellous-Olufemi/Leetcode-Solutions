class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = [nums[0]] * len(nums)
        arr = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
            
            if i >= k:
                arr[i] = pref[i] - pref[i-k+1] + nums[i-k+1]
            else:
                arr[i] = pref[i]

        count = arr[k-1]
        for i in range(k-1, len(nums)):
            count = max(count, arr[i])

            if i+k < len(nums) and arr[i] > 0:
                arr[i+k] += arr[i]

        return count
 