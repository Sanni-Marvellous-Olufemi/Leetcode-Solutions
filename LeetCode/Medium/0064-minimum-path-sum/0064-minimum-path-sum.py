class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        memo = {}

        def walk(r, c):
            nonlocal row, col

            if (r >= row) or (c >= col):
                return float("inf")

            if (r == row-1) and (c == col-1):
                return grid[r][c]

            if (r,c) in memo:
                return memo[(r,c)]

            opt1 = walk(r+1, c)
            opt2 = walk(r, c+1)

            memo[(r,c)] = grid[r][c] + min(opt1, opt2)
            return memo[(r,c)]

        return walk(0,0)
        