class Solution:
    def numOfWays(self, n: int) -> int:
        memo = {}

        def walk(row, prev):
            key = (row, prev)

            if key in memo:
                return memo[key]

            if row == n:
                return 1

            total = 0
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        if a == b or b == c:
                            continue
                        if prev and (a == prev[0] or b == prev[1] or c == prev[2]):
                            continue
                        total += walk(row + 1, (a, b, c))

            memo[key] = total % (10**9 + 7)
            return memo[key]

        return walk(0, None)
