class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ans = None
        count = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and not ans:
                count += 1
                ans = True

            if nums[i] < nums[i-1] and ans or ans is None:
                count += 1
                ans = False

        return ans if (ans == True and count == 3) else False
            