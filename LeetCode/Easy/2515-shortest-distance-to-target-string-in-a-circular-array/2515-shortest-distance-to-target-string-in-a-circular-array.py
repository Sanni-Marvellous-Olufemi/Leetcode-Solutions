class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = float("inf")
        n = len(words)

        for i in range(len(words)):
            if words[i] == target:
                
                prev = startIndex + (n - i) if startIndex < i else (n - startIndex + i)
                curr = abs(startIndex - i)

                ans = min(ans, curr, prev)

        return ans if ans != float("inf") else -1