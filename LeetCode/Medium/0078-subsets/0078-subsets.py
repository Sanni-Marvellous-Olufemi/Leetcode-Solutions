class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dummy = []

        def walk(i):
            ans.append(dummy[:])

            for j in range(i, len(nums)):
                dummy.append(nums[j])
                walk(j+1)
                dummy.pop()

        walk(0)
        return ans   