class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        dummy = []

        def walk(i):
            if i >= len(nums):
                return

            for j in range(i+1, len(nums)):
                dummy.append(nums[j])
                ans.append(dummy[:])
                walk(j)
                dummy.pop()

        for i in range(len(nums)):
            dummy.append(nums[i])
            ans.append(dummy[:])
            walk(i)
            dummy.pop()

        return ans

            