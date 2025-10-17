class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div, non = 0, 0

        for i in range(n+1):
            if i % m == 0:
                div += i
            else:
                non += i

        return non - div