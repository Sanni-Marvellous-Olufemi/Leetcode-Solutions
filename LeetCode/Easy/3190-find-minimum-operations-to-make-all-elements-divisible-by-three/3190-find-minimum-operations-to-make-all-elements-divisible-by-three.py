class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in nums:
            curr = i % 3
            ans += min(curr, 3-curr)

        return ans