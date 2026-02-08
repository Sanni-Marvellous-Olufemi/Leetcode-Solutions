class Solution:
    def minimumDeletions(self, s: str) -> int:
        curr, ans = [], float("inf")

        a, b = 0, 0
        for i in s:
            if i == "a":
                a += 1

        for i in range(len(s)):
            if s[i] == "a":
                a -= 1
            
            ans = min(ans, (a + b))
            b += 1 if s[i] == "b" else 0

        return ans

