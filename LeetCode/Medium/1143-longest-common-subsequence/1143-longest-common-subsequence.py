class Solution:
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