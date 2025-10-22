class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        dif, left, ans = [0] * len(nums), 0, 0

        for right in range(1, len(nums)):
            while nums[right] - nums[left] > (k * 2):
                left += 1

            ans = max(ans, right - left + 1)
            
        return ans

        
            
