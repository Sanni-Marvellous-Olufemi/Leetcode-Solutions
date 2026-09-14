class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def walk(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] =  walk(i+1, j+1) + 1
                return memo[(i, j)]

            memo[(i, j)] = max(walk(i+1, j), walk(i, j+1))
            return memo[(i, j)]

        return walk(0,0)