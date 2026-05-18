class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hashmap = defaultdict(set)
        ans = float("inf")

        for i, num in enumerate(arr):
            hashmap[num].add(i)

        queue = deque()
        sets = set()
        queue.append((0, 0))

        while queue:
            index, dist = queue.popleft()

            if index in sets or index < 0 or index >= len(arr):
                continue

            if index == len(arr) - 1:
                ans = min(ans, dist)
                continue

            sets.add(index)
            node = arr[index]

            if hashmap[node]:
                for i in hashmap[node]:
                    if i != index and i not in sets:
                        queue.append((i, dist+1))

                hashmap[node] = None

            if index+1 not in sets and index+1 < len(arr):
                queue.append((index+1, dist+1))

            if index-1 not in sets and index-1 > 0:
                queue.append((index-1, dist+1))

        return ans