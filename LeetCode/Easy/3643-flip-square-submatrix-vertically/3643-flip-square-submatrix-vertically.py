class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        r1 = x
        r2 = x + k -1

        while r1 < r2:
            for c in range(y, k+y):
                grid[r1][c], grid[r2][c] = grid[r2][c], grid[r1][c]

            r1 += 1
            r2 -= 1

        return grid