class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n, sets = len(grid), len(grid[0]), set()
        count = 0
        

        for r in range(m):
            x = y = 0

            for c in range(-1, n):
                if c < n-1:
                    x += 1 if grid[r][c+1] == "X" else 0
                    y += 1 if grid[r][c+1] == "Y" else 0

                    grid[r][c+1] = [x, y]

                if r > 0 and c >= 0:
                    grid[r][c][0] += grid[r-1][c][0]
                    grid[r][c][1] += grid[r-1][c][1]

        
        def walk(r, c):
            nonlocal m, n, count

            if (r >= m) or (c >= n) or (r,c) in sets:
                return

            if (grid[r][c][0] == grid[r][c][1]) and grid[r][c][0] > 0:
                count += 1

            sets.add((r,c))
            walk(r+1, c) 
            walk(r, c+1)
  
        walk(0, 0)
        return count