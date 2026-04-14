class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float("inf")
        
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(start - i))

        return ans if ans != (float("inf")) else 0
        