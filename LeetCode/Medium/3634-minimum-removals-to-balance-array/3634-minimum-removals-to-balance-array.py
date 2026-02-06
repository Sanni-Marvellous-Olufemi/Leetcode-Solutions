class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        end, ans = 0, 0

        for start in range(len(nums)):
            while end < len(nums) and nums[end] <= nums[start] * k:
                end += 1

            ans = max(ans, end-start) if end < len(nums) else ans

        return len(nums) - ans if ans else 0