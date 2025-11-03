class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashmap, left = defaultdict(int), 0

        for right in range(len(s)):
            sets = set(s[left:right+1])

            if right - left + 1 == minSize:
                hashmap[s[left:right+1]] += 1 if len(sets) <= maxLetters else 0
                left += 1

        return max(hashmap.values()) if hashmap else 0
