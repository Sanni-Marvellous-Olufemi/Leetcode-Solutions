class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = coins[i][j]
                for k in range(3):
                    if i == 0 and j == 0:
                        dp[i][j][0] = val

                        if k > 0:
                            dp[i][j][k] = max(dp[i][j][k], 0 if val < 0 else val)
                        continue
                    
                    res = -float('inf')
                    if i > 0: res = max(res, dp[i-1][j][k])
                    if j > 0: res = max(res, dp[i][j-1][k])
                    
                    dp[i][j][k] = max(dp[i][j][k], res + val)
                    
                    if k > 0:
                        prev_res = -float('inf')
                        if i > 0: prev_res = max(prev_res, dp[i-1][j][k-1])
                        if j > 0: prev_res = max(prev_res, dp[i][j-1][k-1])
                        
                        dp[i][j][k] = max(dp[i][j][k], prev_res)

        return max(dp[m-1][n-1])