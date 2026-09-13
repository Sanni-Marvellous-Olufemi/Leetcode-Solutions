class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        hashmap = {}

        for i in range(1, len(s)+1):
            if s[i-1] in hashmap:
                j = hashmap[s[i-1]]
                dp[i] = (2 * dp[i-1]) - (dp[j])
            else:
                dp[i] = 2 * dp[i-1]

            hashmap[s[i-1]] = i-1

        return (dp[-1] -1) % ((10**9)+7)