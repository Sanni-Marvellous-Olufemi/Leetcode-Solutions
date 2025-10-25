class Solution:
    def totalMoney(self, n: int) -> int:

        def formula(num):
            ans = num * (num+1)//2
            return ans

        if n < 7:
            return formula(n)

        mod = n % 7
        num = n // 7 if not mod else (n//7) + 1
        ans = 0

        for i in range(num):
            curr = i+7 if n > 7 else i+n
            ans += (formula(curr) - formula(i))
            n -= 7

        return ans
        
        