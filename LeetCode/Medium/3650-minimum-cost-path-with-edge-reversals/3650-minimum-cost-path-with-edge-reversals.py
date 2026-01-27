from heapq import heappop, heappush

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        hashmap, sets, heap = {}, set(), []
        heappush(heap, (0,0))

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w*2))
            hashmap[u] = float("inf")
            hashmap[v] = float("inf")
        hashmap[0] = 0

        while heap:
            _, node = heappop(heap)

            if node in sets:
                continue
            sets.add(node)

            for child, edge in graph[node]:
                if child in sets:
                    continue

                if edge + hashmap[node] < hashmap[child]:
                    hashmap[child] = edge + hashmap[node]
                    heappush(heap, (hashmap[child], child))

        return hashmap[n-1] if hashmap[n-1] and hashmap[n-1] != float("inf") else -1