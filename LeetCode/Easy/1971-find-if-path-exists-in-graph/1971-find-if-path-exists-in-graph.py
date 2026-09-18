class Union:
    def __init__(self, n):
        self.graph = {}
        self.rank = {}

        for i in range(n):
            self.graph[i] = i
            self.rank[i] = 1

    def find(self, node):

        if node != self.graph[node]:
            self.graph[node] = self.find(self.graph[node])

        return self.graph[node]

    def union(self, node1, node2):
        a = self.find(node1)
        b = self.find(node2)

        if a == b:
            return

        if self.rank[b] < self.rank[a]:
            self.graph[b] = a
        elif self.rank[b] > self.rank[a]:
            self.graph[a] = b
        else:
            self.graph[b] = a
            self.rank[a] += 1


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        union = Union(n)

        for i, j in edges:
            union.union(i, j)

        if not edges or source not in union.graph or destination not in union.graph:
            return False

        return union.find(source) == union.find(destination)





class Solution1:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashmap = defaultdict(set)

        for i, j in edges:
            hashmap[i].add(j)
            hashmap[j].add(i)

        queue = deque()
        sets = set()
        queue.append(source)
        sets.add(source)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == destination:
                    return True

                for j in hashmap[node]:
                    if j not in sets:
                        queue.append(j)
                        sets.add(j)

        return False