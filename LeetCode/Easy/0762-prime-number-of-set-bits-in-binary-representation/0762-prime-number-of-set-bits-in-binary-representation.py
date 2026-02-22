class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0

        def isPrime(n):
            for j in range(2, int(n ** (1/2))+1):
                if (n/j) == (n//j):
                    return False
            return True if n != 1 else False
                
        for i in range(left, right + 1):
            s = bin(i)
            count = Counter(s)
            ans += 1 if isPrime(count["1"]) else 0


        return ans