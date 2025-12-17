class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return i+2

        

class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sets = set(nums)

        for i in range(1, len(nums)+2):
            if i not in sets:
                return i
        