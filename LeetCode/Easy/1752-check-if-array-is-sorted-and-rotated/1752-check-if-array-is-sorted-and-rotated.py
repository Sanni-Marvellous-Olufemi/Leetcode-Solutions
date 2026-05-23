class Solution:
    def check(self, nums: List[int]) -> bool:
        num = min(nums)
        j = 0
        curr = None

        while j < len(nums):
            if nums[j] == num:
                curr = j if curr is None else curr

                if j > 0 and nums[j] < nums[j-1]:
                    curr = j

            j += 1

        j = curr
        for _ in range(len(nums)-1):
            if nums[j % len(nums)] > nums[(j+1) % len(nums)]:
                return False
            j += 1

        return True