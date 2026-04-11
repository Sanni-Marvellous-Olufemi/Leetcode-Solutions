class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        ans = float("inf")

        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

        for i in hashmap.values():
            if len(i) < 3:
                continue

            for j in range(len(i)-2):
                ans = min(ans, (i[j+1] - i[j]) + (i[j+2] - i[j+1]) + (i[j+2] - i[j]))

        return ans if ans != float("inf") else -1