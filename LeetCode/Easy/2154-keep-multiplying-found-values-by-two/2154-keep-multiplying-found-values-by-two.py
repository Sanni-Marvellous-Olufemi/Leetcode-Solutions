class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()

        while True:
            start, end = 0, len(nums)-1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == original:
                    break
                elif nums[mid] > original:
                    end = mid - 1
                else:
                    start = mid + 1

            if nums[mid] != original:
                break
            original *= 2

        return original