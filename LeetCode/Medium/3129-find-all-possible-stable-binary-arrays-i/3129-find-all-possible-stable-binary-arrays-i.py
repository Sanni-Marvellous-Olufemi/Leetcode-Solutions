class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dp(z, o, last):
            if z == 0 and o == 0:
                return 1
            state = (z, o, last)
            if state in memo:
                return memo[state]
            
            ans = 0
            if last == 1: 
                for i in range(1, min(z, limit) + 1):
                    ans = (ans + dp(z - i, o, 0)) % MOD
            else:
                for i in range(1, min(o, limit) + 1):
                    ans = (ans + dp(z, o - i, 1)) % MOD
            
            memo[state] = ans
            return ans


        return (dp(zero, one, 0) + dp(zero, one, 1)) % MOD