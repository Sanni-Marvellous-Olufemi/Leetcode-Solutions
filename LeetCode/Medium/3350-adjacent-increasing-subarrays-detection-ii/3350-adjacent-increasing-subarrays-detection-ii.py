class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        arr, curr, max_x = [0], 0, 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = i

            arr.append(curr)

        counter = Counter(arr)
        arr = list(counter.keys())
        
        for i in range(1, len(arr)):
            curr = max(counter[arr[i]], counter[arr[i-1]])
            curr = max(curr//2, min(counter[arr[i]], counter[arr[i-1]]))
            max_x = max(max_x, curr)

        max_x = max(max_x, counter[arr[0]]//2)
        return max(max_x, 1)

    