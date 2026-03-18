class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n, sets = len(grid), len(grid[0]), set()

        for r in range(m):
            for c in range(n):
                if c < n-1:
                    grid[r][c+1] += grid[r][c]
                if r > 0:
                    grid[r][c] += grid[r-1][c]

        def walk(r, c):
            nonlocal m, n

            if (r >= m) or (c >= n) or (grid[r][c]) >  k or (r,c) in sets:
                return 0

            sets.add((r,c))
            return walk(r+1, c) + walk(r, c+1) + 1
  
        return walk(0, 0)