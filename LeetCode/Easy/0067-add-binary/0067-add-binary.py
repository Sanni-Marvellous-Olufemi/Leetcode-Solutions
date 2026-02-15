class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count = 0
        n, m = len(a) - 1, len(b) - 1
        ans = ""

        while n >= 0 or m >= 0:
            if n >= 0:
                count += int(a[n])
                n -= 1

            if m >= 0:
                count += int(b[m])
                m -= 1

            ans = str(count % 2) + ans
            count //= 2

        return ans if count == 0 else "1" + ans
