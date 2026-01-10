class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def walk(i, j):
            
            if i >= len(s1) or j >= len(s2):
                return 0

            if (i, j) in memo:
                return memo[(i,j)]

            if s1[i] == s2[j]:
                memo[(i,j)] = walk(i+1, j+1) + ord(s1[i])
                return memo[(i, j)]
                
            memo[(i,j)] = max(walk(i+1, j), walk(i, j+1))

            return memo[(i,j)]
        
        ans = walk(0, 0)
        count = 0

        for i in range(max(len(s1), len(s2))):
            if i < len(s1):
                count += ord(s1[i])
            if i < len(s2):
                count += ord(s2[i])

        return count - ans*2