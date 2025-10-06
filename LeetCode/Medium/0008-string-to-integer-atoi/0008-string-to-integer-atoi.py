class Solution:
    def myAtoi(self, s: str) -> int:
        ans, y, neg = "", False, 1

        for i in s:
            if i == " " and not y:
                continue
            if i.isdigit():
                ans += i
            elif y or i not in {"-", "+"}:
                break

            neg = -1 if i == "-" else neg
            y = True

        return 0 if not ans else (min((int(ans)), ((2 ** 31) - 1)) if neg != -1 else max(int(ans)*-1, (-(2 ** 31))))

"""
-Skip leading white spaces
-Add digits to a string, break if not digit
-Multiply by leading sign and return it
"""