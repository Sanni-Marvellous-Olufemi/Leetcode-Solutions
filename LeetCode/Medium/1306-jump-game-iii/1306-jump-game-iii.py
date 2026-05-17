class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        sets = set()

        # def walk(i):
        #     if i < 0 or i >= len(arr) or i in sets:
        #         return False

        #     if arr[i] == 0:
        #         return True

        #     sets.add(i)
        #     return walk(i + arr[i]) or walk(i - arr[i])

        # return walk(start)

        queue = deque()
        queue.append(start)

        while queue:
            i = queue.popleft()

            if i < 0 or i >= len(arr) or i in sets:
                continue

            if arr[i] == 0:
                return True

            sets.add(i)
            queue.append(i + arr[i])
            queue.append(i - arr[i])

        return False
