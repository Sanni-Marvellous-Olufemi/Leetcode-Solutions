class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ex, ans = 0, 0

        while numBottles > 0:
            ans += numBottles
            numBottles += ex
            ex = numBottles % numExchange
            numBottles //= numExchange 

        return ans
