class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sets = set()
        start = 0

        for i in range(k-1, len(s)):
            sets.add(s[start:i+1])
            start += 1

        return len(sets) == 2 ** k
            