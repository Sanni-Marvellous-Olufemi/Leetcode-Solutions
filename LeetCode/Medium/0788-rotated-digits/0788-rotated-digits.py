class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for i in range(1, n+1):
            num = str(i)

            for j in num:
                if j in {"3", "4", "7"}:
                    break

            else:
                if set(num) <= {"0", "1", "8"}:
                    continue

                ans += 1

        return ans
            