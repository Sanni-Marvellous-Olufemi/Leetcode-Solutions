class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        hashmap = defaultdict(int)

        for i in nums:
           hashmap[i%value] += 1

        for i in range(len(nums) + 1):
            if (i%value not in hashmap) or hashmap[i%value] == 0:
                return i

            hashmap[i%value] -= 1

        