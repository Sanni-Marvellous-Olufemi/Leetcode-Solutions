class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        ans = -1

        if k == len(nums):
            return max(nums)

        for i in nums:
           hashmap[i] += 1

        if k == 1:
            for i in hashmap:
                ans = max(ans, i) if hashmap[i] == 1 else ans
            return ans
        
        ans = max(ans, nums[0]) if hashmap[nums[0]] == 1 else ans
        ans = max(ans, nums[-1]) if hashmap[nums[-1]] == 1 else ans

        return ans