class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if max(Counter(s[i:j+1]).values()) <= 2:
                    ans = max(ans, (j-i)+1)

        return ans
