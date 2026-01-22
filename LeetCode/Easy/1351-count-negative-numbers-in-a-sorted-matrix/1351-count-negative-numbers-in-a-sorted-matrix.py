class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for r in range(len(grid)-1, -1, -1):
            for c in range(len(grid[0])-1, -1, -1):
                if grid[r][c] < 0:
                    count += 1
                else:
                    break

        return count