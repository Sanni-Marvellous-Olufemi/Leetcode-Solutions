class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums, prod = 0, 1
        s = str(n)

        for i in s:
            i = int(i)
            sums += i
            prod *= i

        return (n % (sums+prod)) == 0