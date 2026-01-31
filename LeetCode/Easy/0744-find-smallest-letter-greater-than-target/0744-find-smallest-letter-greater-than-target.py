class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans, y = "z", False

        for i in letters:
            if i > target:
                y = True
                ans = min(ans, i)

        return ans if y else letters[0]