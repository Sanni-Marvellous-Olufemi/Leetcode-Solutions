class Solution:
    def binaryGap(self, n: int) -> int:
        ans, count = 0, 0

        for j, i in enumerate(bin(n)):
            ans = max(ans, count+1) if (i == "1" and j != 2) else ans
            count = count + 1 if i == "0" else 0

        return ans
