class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        ans = ""
        for i in range(numRows):
            down = True
            curr = i

            while curr < len(s):
                if down:
                    formula = 2 * (numRows - 1 - i)
                    down = False
                else:
                    formula = 2 * i
                    down = True
                if formula > 0:
                    ans += s[curr]
                    curr += formula

        return ans
