class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0 

        for i in range(len(nums)):
            sets = set()
            even = 1 if nums[i] % 2 == 0 else 0
            odd = 1 if nums[i] % 2 == 1 else 0
            sets.add(nums[i])

            for j in range(i+1, len(nums)):
                if nums[j] not in sets:
                    sets.add(nums[j])
                    even += 1 if nums[j] % 2 == 0 else 0
                    odd += 1 if nums[j] % 2 == 1 else 0
                
                if even == odd:
                    ans = max(ans, j-i+1)

        return ans