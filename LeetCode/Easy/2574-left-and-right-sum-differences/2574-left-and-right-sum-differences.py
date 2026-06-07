class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = [0 for i in nums]
        left = right = 0

        for i in range(len(nums)):
            j = len(nums)-i-1
            left, right = left+nums[i], right+nums[j]

            if i > j:
                ans[i], ans[j] = abs(left - ans[i]), abs(right - ans[j])
            elif i == j:
                ans[i] = abs(left - right)
            else:
                ans[i], ans[j] = left, right

        return ans        