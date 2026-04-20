class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0

        for i in range(len(colors)):
            if colors[i] != colors[0]:
                ans = max(ans, i)

            if colors[i] != colors[-1]:
                ans = max(ans, len(colors) - 1 - i)

        return ans