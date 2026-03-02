class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # 1. Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        # 2. Greedily satisfy the requirement for each row i
        for i in range(n):
            # Target: row i needs at least (n - 1 - i) trailing zeros
            target = n - 1 - i
            
            # Find the first row at or below i that satisfies the requirement
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
            
            # If no such row is found, it's impossible
            if found_idx == -1:
                return -1
            
            # 3. Move the found row up to the current position i
            # This simulates adjacent swaps
            while found_idx > i:
                trailing_zeros[found_idx], trailing_zeros[found_idx - 1] = \
                    trailing_zeros[found_idx - 1], trailing_zeros[found_idx]
                swaps += 1
                found_idx -= 1
                
        return swaps