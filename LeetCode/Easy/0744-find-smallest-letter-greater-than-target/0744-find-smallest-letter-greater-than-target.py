class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = "z"

        for i in letters:
            if i > target:
                ans = min(ans, i)

        return ans if target != "z" else letters[0]