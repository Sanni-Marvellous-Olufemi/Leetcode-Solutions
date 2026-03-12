class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        def can_form_tree(min_strength):
            dsu = DSU(n)
            upgrades_remaining = k
            edges_count = 0
            
            for u, v, s, m in edges:
                if m == 1:
                    if s < min_strength: return False
                    if not dsu.union(u, v): return False 
                    edges_count += 1
            
            for u, v, s, m in edges:
                if m == 0 and s >= min_strength:
                    if dsu.union(u, v):
                        edges_count += 1
            
            for u, v, s, m in edges:
                if m == 0 and s < min_strength and s * 2 >= min_strength:
                    if upgrades_remaining > 0 and dsu.union(u, v):
                        upgrades_remaining -= 1
                        edges_count += 1
            
            return edges_count == n - 1

        low = 0
        high = 200000 
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_tree(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans