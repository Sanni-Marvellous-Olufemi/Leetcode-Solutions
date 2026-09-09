class Solution:
    def countCommas(self, n: int) -> int:
        curr = [999,999999,999999999,999999999999,999999999999999]
        count = 0

        for i in range(len(curr)):
            if n < curr[i]:
                return count

            if i < len(curr)-1 and n > curr[i+1]:
                count += ((curr[i+1] - curr[i]) * (i+1))
            else:
                count += ((n - curr[i]) * (i+1))

        return count