class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def walk(i, k):
            if k < 0 or i >= len(coins):
                return float("inf")

            if k == 0:
                return 0

            if (i, k) in memo:
                return memo[(i, k)]

            memo[(i, k)] = min(walk(i+1, k), walk(i, k - coins[i]) + 1)
            return memo[(i, k)]
        
        ans = walk(0, amount)

        return ans if ans != float("inf") else -1