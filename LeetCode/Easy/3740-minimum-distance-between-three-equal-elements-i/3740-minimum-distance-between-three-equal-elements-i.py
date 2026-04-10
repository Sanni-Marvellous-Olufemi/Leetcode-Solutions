class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        min_dist = float('inf')
        
        for indices in index_map.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                a, b, c = indices[i], indices[i+1], indices[i+2]
                dist = 2 * (c - a)
                min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1