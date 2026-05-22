class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        ans = 0

        # Find the index rotation stops / original sorted list began
        while lo <= hi:
            mid = (hi + lo) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                ans = mid
                break
            elif nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1

        start, end = 0, len(nums) - 1
        if ans != 0:
            # If rotated and target > last number in list:
            # Target is between start of list and end of rotation
            if target > nums[end]:
                end = ans - 1
            # If rotated and target < last number in list:
            # Target is between end of rotation and end of list
            else:
                start = ans

        while start <= end:
            ans = (end + start) // 2

            if target == nums[ans]:
                return ans
            elif target > nums[ans] :
                start = ans + 1
            elif target < nums[ans] :
                end = ans - 1

        return -1