class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(values)):
            u, v = equations[i]
            e = values[i]
            graph[u].append((v, e))
            graph[v].append((u, 1/e))

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
                continue

            queue = deque()
            sets = set()
            queue.append((start, 1))
            y = False

            while queue:
                node, e = queue.popleft()

                if node in sets:
                    continue
                sets.add(node)

                if node == end:
                    ans.append(e)
                    y = True
                    break

                for child, w in graph[node]:
                    if child in sets:
                        continue

                    queue.append((child, e * w))

            if not y:
                ans.append(-1.0)

        return ans
                    
