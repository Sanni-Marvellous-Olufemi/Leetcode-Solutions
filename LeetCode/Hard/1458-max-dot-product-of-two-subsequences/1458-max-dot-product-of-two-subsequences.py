class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}

        def walk(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return float("-inf")

            if (i, j) in memo:
                return memo[(i,j)]

            take = max(0, walk(i+1, j+1)) + (nums1[i] * nums2[j])
            skip = max(walk(i, j+1), walk(i+1, j))

            memo[(i,j)] = max(take, skip)
            return memo[(i,j)]

        return walk(0,0)