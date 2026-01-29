from heapq import heappop, heappush

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        ans = 0

        for i in range(len(original)):
            graph[original[i]].append((changed[i], cost[i]))

        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            start, end = source[i], target[i]
            heap, sets, hashmap = [], set(), defaultdict(lambda: float("inf"))

            hashmap[start] = 0
            heappush(heap, (0, start))

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

            if end not in hashmap:
                return -1
            ans += hashmap[end]

        return ans

        