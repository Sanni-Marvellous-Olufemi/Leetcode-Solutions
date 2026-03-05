class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        ans = s[0]
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                count += 1
                ans += "1" if s[i] == "0" else "0"
            else:
                ans += s[i]


        ans = "1" if s[0] == "0" else "0"
        count2 = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                count2 += 1
                ans += "1" if s[i] == "0" else "0"
            else:
                ans += s[i]


        return min(count, count2)
        