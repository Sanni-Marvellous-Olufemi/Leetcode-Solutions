class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0

        for c in range(len(matrix[0])):
            for r in range(1, len(matrix)):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]

        for r in range(len(matrix)):
            matrix[r].sort(reverse=True)

            for c, height in enumerate(matrix[r]):
                if height == 0: break 
                ans = max(ans, height * (c + 1))
                
        return ans
