class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(values)):
            u, v = equations[i]
            e = values[i]
            graph[u].append((v, e))
            graph[v].append((u, 1/e))

        def walk(start, end):
            if start not in graph or end not in graph:
                return -1.0

            queue = deque()
            sets = set()
            queue.append((start, 1))

            while queue:
                node, e = queue.popleft()

                if node in sets:
                    continue
                sets.add(node)

                if node == end:
                    return e

                for child, w in graph[node]:
                    if child in sets:
                        continue

                    queue.append((child, e * w))
            return -1.0

        for start, end in queries:
            ans.append(walk(start, end))

        return ans
                    
