class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans, x, y = 0, points[0][0], points[0][1]

        for i in range(1, len(points)):
            if x == points[i][0]:
                ans += abs(y - points[i][1])
            elif y == points[i][1]:
                ans += abs(x - points[i][0])
            else:
                ans += max(abs(x-points[i][0]), abs(y - points[i][1]))

            x, y = points[i][0], points[i][1]

        return ans