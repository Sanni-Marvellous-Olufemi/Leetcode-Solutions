class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # 25 + sum(nums) - (n) * n-i

        curr = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            curr += (num * i)
        
        ans = curr
        for i in range(1, len(nums)):
            curr = (curr + total) - ((len(nums)) * nums[len(nums) - i])
            ans = max(curr, ans)

        return ans