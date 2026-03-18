class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count, sets = 0, set()

        for r in range(m):
            for c in range(n):
                if c < n-1:
                    grid[r][c+1] += grid[r][c]
                if r > 0:
                    grid[r][c] += grid[r-1][c]

        def walk(r, c):
            nonlocal m, n, count

            if (r >= m) or (c >= n) or (grid[r][c]) >  k or (r,c) in sets:
                return 

            count += 1
            sets.add((r,c))
            walk(r+1, c)
            walk(r, c+1)

        walk(0, 0)
        return count