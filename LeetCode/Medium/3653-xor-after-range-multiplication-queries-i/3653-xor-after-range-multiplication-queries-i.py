class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        for l, r, k, v in queries:

            while l <= r:
                nums[l] = (nums[l] * v) % ((10 ** 9) + 7)
                l += k

        ans = nums[0]

        for i in range(1, len(nums)):
            ans ^= nums[i]

        return ans