class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        """
            0 1 2 3 4 5 6

        0   1 0 0 0 0 0 0
        1   1 1 0 0 0 0 0
        2   1 1 1 0 0 0 0
        3   1 1 1 1 0 0 0
        4   1 1 1 2 1 0 0
        5   1 1 1 3 3 0 0
        6   1 1 1 3 3 3 0
        7   1 1 1 3 3 3 3
        """

        dp = [[0 for i in range(len(t)+1)] for i in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        prev = 0
        memo = {}

        def walk(i, j):
            nonlocal prev

            if i >= len(s) or j >= len(t) or len(s)-i < len(t)-j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            curr = 0

            if s[i] == t[j]:
                if j == len(t)-1:
                    curr += 1

                curr += walk(i+1, j+1)
            
            curr += walk(i+1, j)
            memo[(i,j)] = curr
            return curr

        return walk(0, 0)
            
