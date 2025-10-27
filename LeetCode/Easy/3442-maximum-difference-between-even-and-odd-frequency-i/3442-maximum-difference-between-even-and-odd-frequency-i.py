class Solution:
    def maxDifference(self, s: str) -> int:
        arr = Counter(s).values()
        start, end = float("inf"), 0

        for i in arr:
            if i % 2 == 0 and i < start:
                start = i

            if i % 2 == 1 and i > end:
                end = i

        return end - start