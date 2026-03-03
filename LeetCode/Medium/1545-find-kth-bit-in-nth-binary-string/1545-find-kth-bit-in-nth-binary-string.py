class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(num):
            ans = ""

            for i in num:
                if i == "1":
                    ans += "0"
                else:
                    ans += "1"
            return ans
        
        def walk(n):
            if n == 1:
                return "0"

            num = walk(n - 1)

            return num + "1" + invert(num)[::-1]

        return walk(n)[k-1]