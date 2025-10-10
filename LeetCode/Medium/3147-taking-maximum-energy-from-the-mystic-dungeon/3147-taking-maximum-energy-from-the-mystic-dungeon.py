class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        for i in range(len(energy)):
            if i - k >= 0:
                energy[i] = max(energy[i] + energy[i - k], energy[i])

        for i in range(len(energy) - k, len(energy)):
            ans = max(ans, energy[i])

        return ans


"""
-Use prefix sum to calculate the sum of all indices. Calculate it so that each index has the sum of all i % k indices before it.
-But don't use a blind prefix sum. Use a kadanes prefix sum so that each index has the max of all i % k indices before it. So if the current index is greater than the i % k sum, it greedily picks the current index instead of adding the current index value to the i % k sum
-When you're done creating the kadane's prefix sum array, iterate through the last k elements and return the max 
"""
