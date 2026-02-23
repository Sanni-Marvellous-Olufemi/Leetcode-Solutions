class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sets = set(s[i-k+1:i+1] for i in range(k-1, len(s)))
        return len(sets) == 2 ** k
            