class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for r in range(m):
            for c in range(n):
                if c < n-1:
                    grid[r][c+1] += grid[r][c]
                if r > 0:
                    grid[r][c] += grid[r-1][c]
  
                count += 1 if grid[r][c] <= k else 0

        return count