class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        if s[0] == "0" or "00" in s:
            return 0

        def walk(i):
            if i < len(s) and s[i] == "0":
                return 0

            if i >= len(s)-1:
                return 1
            
            if i in memo:
                return memo[i]

            opt1 = 0
            if (s[i] == "2") and (i < len(s)-1) and (s[i+1] <= "6"):
                opt1 = walk(i+2)

            if (s[i] == "1"):
                opt1 = walk(i+2)

            opt2 = walk(i+1)
            memo[i] = opt1 + opt2
            return memo[i]

        return walk(0)

            