class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for i in range(num1, num2+1):
            num = str(i)
            for j in range(1, len(num)-1):
                if (num[j-1] < num[j] and num[j] > num[j+1]) or num[j-1] > num[j] and num[j] < num[j+1]:
                    ans += 1

        return ans