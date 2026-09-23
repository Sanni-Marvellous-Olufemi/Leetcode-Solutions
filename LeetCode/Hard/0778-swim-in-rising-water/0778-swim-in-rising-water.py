class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]

        seen = {(0, 0)}

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while heap:
            time, row, col = heappop(heap)

            if row == n-1 and col == n-1:
                return time

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if not (0 <= nr < n):
                    continue

                if not (0 <= nc < n):
                    continue

                if (nr, nc) in seen:
                    continue

                seen.add((nr, nc))

                new_time = max(time, grid[nr][nc])

                heappush(heap, (new_time, nr, nc))

        return -1

"""
use min heap so I always traverse lowest cost each time
"""