class Solution:
    def fib(self, n: int) -> int:
        hashmap = {}
        def climb(n):
            if n <= 1:
                return n

            if n in hashmap:
                return hashmap[n]

            hashmap[n] = self.fib(n-1) + self.fib(n-2)
            return hashmap[n]

        return climb(n)


        