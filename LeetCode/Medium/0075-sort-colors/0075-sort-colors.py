class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums)-1

        for mid in range(len(nums)):

            while left <= mid <= right:
                if nums[mid] == 0:
                    nums[mid], nums[left] = nums[left], nums[mid]
                    left += 1

                elif nums[mid] == 2:
                    nums[mid], nums[right] = nums[right], nums[mid]
                    right -= 1

                else:
                    break

            if mid >= right:
                break