class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        curr, arr = 0, [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = i

            arr[i] = curr

        for i in range(len(nums)-(k*2)+1):
            j = i+k
            if arr[i] == arr[i+k-1] and arr[j] == arr[j+k-1]:
                return True

        return False