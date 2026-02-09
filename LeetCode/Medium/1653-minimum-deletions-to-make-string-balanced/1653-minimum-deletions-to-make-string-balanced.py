class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b, ans = s.count("a"), 0, float("inf")

        for i in range(len(s)):
            if s[i] == "a":
                a -= 1
            
            ans = min(ans, (a + b))
            b += 1 if s[i] == "b" else 0

        return ans

