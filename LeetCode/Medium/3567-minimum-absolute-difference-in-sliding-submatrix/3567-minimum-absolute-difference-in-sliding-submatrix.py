from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                values = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.add(grid[x][y])

                sorted_vals = sorted(values)

                if len(sorted_vals) <= 1:
                    ans[i][j] = 0
                else:
                    min_diff = float('inf')
                    for p in range(1, len(sorted_vals)):
                        min_diff = min(min_diff, sorted_vals[p] - sorted_vals[p - 1])
                    ans[i][j] = min_diff

        return ans