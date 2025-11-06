class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        offline, ans = set(), []

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        for check, node in queries:
            if check == 2:
                offline.add(node)
            else:
                if node not in offline:
                    ans.append(node)
                else:
                    sub = -1
                    queue, sets, heap = deque(), set(), []
                    queue.append(node)

                    while queue:
                        curr = queue.popleft()
                        sets.add(curr)
                        for child in graph[curr]:
                            if child in sets:
                                continue
                            
                            if child not in offline:
                                heappush(heap, child)
                            queue.append(child)

                    ans.append(heap[0]) if heap else ans.append(-1)

        return ans             
                    
                    

        return ans

