class Solution:
    def numSub(self, s: str) -> int:
        ans, count = 0, 0

        for i in range(len(s)):
            if s[i] == "1":
                ans += count + 1
                count += 1
            else:
                count = 0

        return ans

"""
Use the pattern
(num of substrings with all 1's) += (num of prev consecutive 1's) + 1

e.g Using the above formula (sub = sub + num + 1)

substrings(sub) = 0, num of prev consecutive(num) = 0

"1" = 1   (sub = 0 + 0 + 1), (updated sub = 1, num = 1)
"11" = 3  (sub = 1 + 1 + 1), (updated sub = 3, num = 2)
"111" = 6  (sub = 3 + 2 + 1), (updated sub = 6, num = 3)
"1111" = 10 (sub = 6 + 3 + 1), (updated sub = 10, num = 4)
"""