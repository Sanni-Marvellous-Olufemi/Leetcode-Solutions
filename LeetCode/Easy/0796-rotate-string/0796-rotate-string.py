class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in (s+s) if len(goal) == len(s) and set(goal) == set(s) else False