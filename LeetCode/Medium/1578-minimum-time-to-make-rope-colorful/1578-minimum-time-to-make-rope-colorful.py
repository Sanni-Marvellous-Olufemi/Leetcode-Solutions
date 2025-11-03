class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count = 0

        for i in range(len(colors)):
            if i < len(colors)-1 and colors[i] == colors[i+1]:
                count += min(neededTime[i], neededTime[i+1])
                neededTime[i+1] = max(neededTime[i], neededTime[i+1])

        return count