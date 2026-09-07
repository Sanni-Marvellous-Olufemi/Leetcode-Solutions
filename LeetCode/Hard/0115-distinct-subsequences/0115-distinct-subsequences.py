class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = 0
        memo = {}

        def walk(i, j):
            nonlocal prev

            if i >= len(s) or j >= len(t) or len(s)-i < len(t)-j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            curr = 0

            if s[i] == t[j]:
                if j == len(t)-1:
                    curr += 1

                curr += walk(i+1, j+1)
            
            curr += walk(i+1, j)
            memo[(i,j)] = curr
            return curr

        return walk(0, 0)
            
