class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        hashmap = {}
        ans = float("inf")

        for i in range(len(nums)):
            if nums[i] in hashmap:
                ans = min(ans, i - hashmap[nums[i]])

            rev = int(str(nums[i])[::-1])
            hashmap[rev] = i

        return ans if ans != float("inf") else -1