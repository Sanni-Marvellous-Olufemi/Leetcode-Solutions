class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        i, j = len(nums1)-1, len(nums2)-1

        while i >= 0 and j >= 0:
            if i >= j:
                i -= 1
                continue

            if nums2[j] >= nums1[i]:
                ans = max(ans, j-i)
                i -= 1
            else:
                j -= 1

        return ans