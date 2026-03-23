class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def calc(l, r, c):
            a = []

            for i in l:
                if i == None:
                    continue
                a.append(i)

            return (min(a) * grid[r][c], max(a) * grid[r][c])

        def walk(r,c):
            nonlocal m, n

            if r == m-1 and c == n-1:
                return [grid[r][c], grid[r][c]]

            if r >= m or c >= n:
                return (None, None)

            if (r, c) in memo:
                return memo[(r,c)]

            a,b = walk(r+1, c)
            d,e = walk(r, c+1)

            memo[(r,c)] =  calc([a,b,d,e], r, c)
            return memo[(r,c)]

        a = max(walk(0, 0))
        
        return a % ((10**9)+7) if a > -1 else -1