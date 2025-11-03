class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashmap, left = defaultdict(int), 0

        for right in range(len(s)):
            sets = set(s[left:right+1])

            if right - left + 1 == minSize:
                hashmap[s[left:right+1]] += 1 if len(sets) <= maxLetters else 0
                left += 1

        return max(hashmap.values()) if hashmap else 0

"""
-If a subarray of len maxSize is repeated, then all subarrays of that subarray were also repeated, so you only need to take note of minSize
-Use a sliding window of len minSize to track subarrays
-For each subarray, convert it to a set. If the length of the set is less than or equal to maxLetters, increase the value of the subarray in the hashmap by 1
-Return Max Hahsmap
"""