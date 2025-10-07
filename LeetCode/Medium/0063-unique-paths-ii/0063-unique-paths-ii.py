class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def walk(r,c):
            nonlocal row, col

            if (r >= row) or (c >= col) or (obstacleGrid[r][c] == 1):
                return 0 

            if (r == row-1) and (c == col-1):
                return 1

            if (r,c) in memo:
                return memo(r,c)

            opt1 = walk(r+1, c)
            opt2 = walk(r, c+1)
            memo[(r,c)] = opt1 + opt2

            return memo[(r,c)]

        return walk(0, 0)