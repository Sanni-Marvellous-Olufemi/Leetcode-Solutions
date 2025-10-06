class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def walk(r, c):
            nonlocal m,n
            if (r >= m) or (c >= n):
                return 0

            if r == m-1 and c == n-1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            opt1 = walk(r, c+1)
            opt2 = walk(r+1, c)
            memo[(r,c)] = opt1 + opt2

            return memo[(r,c)]

        return walk(0,0)