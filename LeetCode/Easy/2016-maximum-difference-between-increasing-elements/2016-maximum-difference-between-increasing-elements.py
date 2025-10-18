class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr, ans = nums[0], -1

        for i in nums:
            if curr < i:
                ans = max(ans, i - curr)

            if curr > i:
                curr = i

        return ans