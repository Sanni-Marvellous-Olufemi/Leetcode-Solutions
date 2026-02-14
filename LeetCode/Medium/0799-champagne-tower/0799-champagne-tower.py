class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = {}
        
        def walk(r, c):
            nonlocal poured, query_row, query_glass

            if (r < 0) or (r > query_row) or (c < 0) or (c > query_glass):
                return 0

            if r == 0 and c == 0:
                return poured

            if (r,c) in memo:
                return memo[(r,c)]

            left = max((walk(r-1, c-1)-1)/2, 0)
            right = max((walk(r-1, c)-1)/2, 0)
            memo[(r,c)] = left + right

            return left + right

        return min(walk(query_row, query_glass), 1)