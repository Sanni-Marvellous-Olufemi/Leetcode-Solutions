class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pref1, pref2, front, back = [], [0] * len(nums), 0, 0

        for i in range(len(nums)):
            j = len(nums) -i -1
            front += nums[i]
            pref1.append(front)
            back += nums[j]
            pref2[j] = back

        count = 0
        for i in range(len(nums)-1):
            count += 1 if abs(pref1[i] - pref2[i+1]) % 2 == 0 else 0

        return count