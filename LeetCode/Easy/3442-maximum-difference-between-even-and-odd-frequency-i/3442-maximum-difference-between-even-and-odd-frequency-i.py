class Solution:
    def maxDifference(self, s: str) -> int:
        arr = sorted(Counter(s).values())
        
        start, end = 0, len(arr)-1

        while start < len(arr) and arr[start] % 2 == 1:
            start += 1

        while end >= 0 and arr[end] % 2 == 0:
            end -= 1

        return arr[end] - arr[start]
