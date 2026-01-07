class Solution(object):
    def convert(self, s, numRows):
        ans = ""

        if numRows == 1:
            return s
        
        for i in range(numRows):
            j = i
            mid =(numRows - 1 - i) * 2
            start = numRows * 2 - 2
            y = False if i in {0, numRows-1} else True

            while j < len(s):
                ans += s[j]

                if y and (j + mid) < len(s):
                    ans += s[j + mid]

                j += start

        return ans

        