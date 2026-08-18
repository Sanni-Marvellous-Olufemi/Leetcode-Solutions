class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        sets = set()
        hashmap = defaultdict(list)
        ans = -1

        if k == len(nums):
            return max(nums)

        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

        for i in hashmap:
            arr = hashmap[i]

            if (len(arr) == 1) and ((arr[0] in {0, len(nums)-1}) or k == 1):
                ans = max(ans, i)

        return ans