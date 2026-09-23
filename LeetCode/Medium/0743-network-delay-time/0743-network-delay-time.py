class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        hashmap = {}

        for i in range(1, n+1):
            hashmap[i] = float("inf")

        hashmap[k] = 0
        heap = []
        heappush(heap, (0, k))
        sets = set()

        while heap:
            w, node = heappop(heap)
            if node in sets:
                continue
            sets.add(node)

            for child, weight in graph[node]:
                if child in sets:
                    continue

                if weight + w < hashmap[child]:
                    hashmap[child] = weight + w
                
                heappush(heap, (hashmap[child], child))
            
            # sets.remove(node)

        ans = max(hashmap.values())
        return ans if ans != float("inf") else -1