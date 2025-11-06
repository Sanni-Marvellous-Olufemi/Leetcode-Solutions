class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        offline, ans, sets = set(), [], set()
        count, hashmap = 0, defaultdict(list)

        for u,v in connections:
            if not graph[u]:
                graph[u].append([])
            if not graph[v]:
                graph[v].append([])
            graph[u][0].append(v)
            graph[v][0].append(u)

        for node in graph:
            if node in sets:
                continue

            count += 1
            queue = deque()
            queue.append(node)

            while queue:
                curr = queue.popleft()
                graph[curr].append(count)
                heappush(hashmap[count], curr)
                sets.add(curr)

                for child in graph[curr][0]:
                    if child in sets:
                        continue
                
                    queue.append(child)

        for i,j in queries:
            if i == 2:
                offline.add(j)
            else:
                if j not in offline:
                    ans.append(j)
                else:
                    station = graph[j][1] if graph[j] else 0
                    add = -1
                    while hashmap[station]:
                        if hashmap[station][0] in offline:
                            heappop(hashmap[station])
                        else:
                            add = hashmap[station][0]
                            break

                    ans.append(add)

        return ans