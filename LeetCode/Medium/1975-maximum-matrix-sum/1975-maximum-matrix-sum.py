class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        pos, neg, count, sums = float("inf"), -float("inf"), 0, 0

        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[r][c] < 0:
                    count += 1
                    neg = max(neg, matrix[r][c])
                    matrix[r][c] *= -1
                    sums += matrix[r][c]

                else:
                    pos = min(pos, matrix[r][c])
                    sums += matrix[r][c]

        if count > 0 and count % 2 == 0:
            return sums
        
        return sums - (min(abs(pos), abs(neg)) * 2)

