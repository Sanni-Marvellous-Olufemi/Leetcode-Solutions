class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def walk(i, j):
            if i >= len(s1) or j >= len(s2):
                if i >= len(s1) and j >= len(s2):
                    return 0
                elif i >= len(s1):
                    return ord(s2[j])
                else:
                    return ord(s1[i])

            if (i, j) in memo:
                return memo[(i,j)]

            if s1[i] == s2[j]:
                memo[(i,j)] = walk(i+1, j+1)
                return memo[(i, j)]
                
            ans = min(walk(i+1, j) + ord(s1[i]), walk(i, j+1) + ord(s2[j]), walk(i+1, j+1) + ord(s1[i]) + ord(s2[j]))
            memo[(i,j)] = ans

            return ans
        
        return walk(0, 0)