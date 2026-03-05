class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count += 1 if (i % 2 == 0 and s[i] == "0") or (i % 2 == 1 and s[i] == "1") else 0

        return min(count, len(s) - count)
        