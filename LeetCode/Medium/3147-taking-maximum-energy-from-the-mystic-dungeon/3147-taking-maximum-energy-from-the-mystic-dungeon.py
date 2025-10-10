class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        for i in range(len(energy)):
            if i - k >= 0:
                energy[i] = max(energy[i] + energy[i-k], energy[i])

        for i in range(len(energy)-k, len(energy)):
            ans = max(ans, energy[i])

        return ans
        