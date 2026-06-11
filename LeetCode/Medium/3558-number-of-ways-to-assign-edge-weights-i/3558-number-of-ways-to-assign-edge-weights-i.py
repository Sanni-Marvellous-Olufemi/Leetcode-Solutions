class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        depth = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque()
        sets = set()
        queue.append((1, 0))

        while queue:
            node, edge = queue.popleft()
            depth = max(depth, edge)

            if node in sets:
                continue
            sets.add(node)

            for child in graph[node]:
                if child in sets:
                    continue
                
                queue.append((child, edge+1))

        return (2 ** (depth - 1)) % ((10**9) + 7) 