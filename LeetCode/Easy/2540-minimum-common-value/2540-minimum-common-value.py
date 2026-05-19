class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0

        for i in nums1:

            while j < len(nums2) and i > nums2[j]:
                j += 1

            if j < len(nums2) and i == nums2[j]:
                return i

        return -1