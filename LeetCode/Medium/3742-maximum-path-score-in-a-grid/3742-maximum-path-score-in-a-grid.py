class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0

        for j in range(n - 1):
            val_next = grid[0][j + 1]
            cost_inc = 1 if val_next > 0 else 0
            for c in range(k + 1 - cost_inc):
                if dp[j][c] != -1:
                    nc = c + cost_inc
                    if dp[j][c] + val_next > dp[j + 1][nc]:
                        dp[j + 1][nc] = dp[j][c] + val_next

        for i in range(1, m):
            next_dp = [[-1] * (k + 1) for _ in range(n)]

            for j in range(n):
                val_ij = grid[i][j]
                cost_inc = 1 if val_ij > 0 else 0
                for c in range(k + 1 - cost_inc):
                    if dp[j][c] != -1:
                        nc = c + cost_inc
                        if dp[j][c] + val_ij > next_dp[j][nc]:
                            next_dp[j][nc] = dp[j][c] + val_ij

            for j in range(n - 1):
                val_next = grid[i][j + 1]
                cost_inc = 1 if val_next > 0 else 0
                for c in range(k + 1 - cost_inc):
                    if next_dp[j][c] != -1:
                        nc = c + cost_inc
                        if next_dp[j][c] + val_next > next_dp[j + 1][nc]:
                            next_dp[j + 1][nc] = next_dp[j][c] + val_next

            dp = next_dp

        ans = max(dp[n - 1])
        return ans if ans >= 0 else -1