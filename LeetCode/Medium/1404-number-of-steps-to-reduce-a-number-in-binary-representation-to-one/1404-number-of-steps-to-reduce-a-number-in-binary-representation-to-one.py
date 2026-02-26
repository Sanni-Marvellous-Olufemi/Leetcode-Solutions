class Solution:
    def numSteps(self, s: str) -> int:
        n, count = int(s, 2), 0

        while n > 1:
            if n % 2 == 1:
                count += 1
                n += 1

            n /= 2
            count += 1

        return count