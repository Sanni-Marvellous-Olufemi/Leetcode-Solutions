class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        curr1, curr2 = 1, 2

        for i in range(3, len(nums)):
            
            if nums[i] <= nums[curr2] or nums[i] <= nums[curr1]:
                # print(nums[i], nums[curr2], nums[curr1])
                if nums[curr2] <= nums[curr1]:
                    curr1 = curr2
                curr2 = i

        return ans + nums[curr1] + nums[curr2]