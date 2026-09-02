class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn, maxx, n = min(nums), max(nums), len(nums)
        ans, arr = 0, [-1, -1]
        
        for i in range(len(nums)):
            if nums[i] == minn or nums[i] == maxx:
                if arr[0] == -1:
                    arr[0] = i
                else:
                    arr[1] = i
                    break

        return min(arr[1]+1, n-arr[0], (arr[0]+1)+(n-arr[1])) if len(nums) > 1 else 1