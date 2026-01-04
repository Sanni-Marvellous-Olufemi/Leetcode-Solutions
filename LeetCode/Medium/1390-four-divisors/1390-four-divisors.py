class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            count, curr, sqrt = 0, 0, int(num ** (1/2))

            for i in range(1, sqrt+1):
                if num % i == 0:
                    count += 2 if (num/i) > sqrt else 1
                    curr += i
                    curr += num / i if (num/i) > sqrt else 0

            ans += (curr) if count == 4 else 0

        return int(ans)