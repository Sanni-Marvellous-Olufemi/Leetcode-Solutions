class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        while True:
            minPair = (-1, -1, float("inf"))
            y = True
            for i in range(1, len(nums)):
                if nums[i]+nums[i-1] <= minPair[2]:
                    minPair = (i-1, i, nums[i]+nums[i-1])

                if nums[i] < nums[i-1]:
                    y = False

            if y:
                break

            nums = nums[:minPair[0]] + [minPair[2]] + nums[minPair[1]+1:]
            count += 1

        return count
