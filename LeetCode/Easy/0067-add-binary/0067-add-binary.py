class Solution:
    def addBinary(self, a: str, b: str) -> str:
        curr, ans = 0, ""

        for i in range(-1, -1-max(len(a), len(b)), -1):
            curr += int(a[i]) if i >= -len(a) else 0
            curr += int(b[i]) if i >= -len(b) else 0
            ans = str(curr % 2) + ans
            curr //= 2

        ans = str(curr % 2) + ans if curr else ""
        return ans

        