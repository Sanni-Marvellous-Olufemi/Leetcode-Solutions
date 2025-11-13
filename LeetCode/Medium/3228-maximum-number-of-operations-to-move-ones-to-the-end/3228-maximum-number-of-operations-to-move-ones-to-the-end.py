class Solution:
    def maxOperations(self, s: str) -> int:
        count, y, ans = 0, False, 0

        for i in range(len(s)):
            if s[i] == "1":
                ans += count if not y else 0
                count += 1
                y = True
            else:
                y = False
                
        return ans
